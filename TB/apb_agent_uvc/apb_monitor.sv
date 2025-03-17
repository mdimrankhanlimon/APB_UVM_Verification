
class apb_monitor extends uvm_monitor;
    `uvm_component_utils(apb_monitor)

    virtual apb_interface apb_mintf;
    apb_seq_item apb_mitem;
	
	// transaction tracing
	int ok;

    uvm_analysis_port #(apb_seq_item) apb_mntr_port;

    // variable declaration for Log file 
	bit apb_mntr_log;
    int file_handle;
    string log_filename = "apb_monitor.log"; 
    int start_time;
    int end_time;
    int transaction_count;

    function new(string name = "apb_monitor", uvm_component parent = null);
        super.new(name, parent);
    endfunction

    // Function to open the log file
    function void set_log_file();
        file_handle = $fopen(log_filename, "w");
        if (file_handle == 0)
            `uvm_error(get_type_name(), $sformatf("Failed to open log file: %s", log_filename));
        $fwrite(file_handle, "| ---- | --------------- | --------------- | ------- | ------------- | --------- | ----------- | ----------- | \n");
        $fwrite(file_handle, "| SL   | Start Time (ps) | End Time (ps)   | Strobe  | Address (hex) | Operation | Data (hex)  | Response    | \n");
        $fwrite(file_handle, "| ---- | --------------- | --------------- | ------- | ------------- | --------- | ----------- | ----------- | \n");
    endfunction

	// function to write log file 
	function void log_file_write();
      	transaction_count++;  			// count the transactions

        // Logging in the specified format
        $fwrite(file_handle, "| %-4d | %-15t | %-15t | %-07b | %-13h | %-9s | %-11h | %-8s | \n",
            transaction_count, start_time, end_time, apb_mitem.PSTRB_i, apb_mitem.PADDR_i,
            (apb_mitem.PWRITE_i ? "Write" : "Read"),
            (apb_mitem.PWRITE_i ? apb_mitem.PWDATA_i : apb_mitem.PRDATA_o),
            (apb_mitem.PSLVERR_o ? "ERROR" : "OKAY"));
       	$fwrite(file_handle, "| ---- | --------------- | --------------- | ------- | ------------- | --------- | ----------- | -------- | \n");
	endfunction                                                                                                                         
	
	virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (!uvm_config_db #(virtual apb_interface)::get(this, "*", "APB_INTF", apb_mintf))
            `uvm_error(get_full_name(), "Could not get apb interface from monitor");

        apb_mntr_port = new("apb_mntr_port", this);
		if(apb_mntr_log) begin 
				set_log_file();
		end
		else `uvm_warning(get_name(), "Monitor log file not created")
    endfunction

    virtual task run_phase(uvm_phase phase);
        forever begin
            @(apb_mintf.cb_mntr);

			// tracing the start time of the transaction
            start_time = $realtime;
		
			//`uvm_info(get_name(), "Monitoring VALID APB signals", UVM_HIGH)
			if (!apb_mintf.PRESETn_i) begin
                    apb_mitem = apb_seq_item::type_id::create("apb_mitem");
                    apb_mitem.PRESETn_i = apb_mintf.PRESETn_i;
					apb_mntr_port.write(apb_mitem);	
			end else begin // Reset deactivated
			`uvm_info(get_name(), "Reset deactivated", UVM_HIGH)		
                if (apb_mintf.cb_mntr.PSEL_i) begin // Select asserted
                    apb_mitem = apb_seq_item::type_id::create("apb_mitem");

					if (apb_mintf.cb_mntr.PENABLE_i) begin
						`uvm_info(get_name(), "PENABLE High at the same cycle of PSEL high", UVM_HIGH)
						apb_mitem.pt_err = 1;
					end

					`uvm_info(get_name(), "PSELECT asserted", UVM_HIGH)

					ok = begin_tr(apb_mitem, "APB_MONITOR_PACKET");

                    apb_mitem.PADDR_i = apb_mintf.cb_mntr.PADDR_i;
                    apb_mitem.PWRITE_i = apb_mintf.cb_mntr.PWRITE_i;
                    apb_mitem.PRESETn_i = apb_mintf.PRESETn_i;

                    if (apb_mintf.cb_mntr.PWRITE_i) begin // For write Transfer
  						`uvm_info(get_name(), "Detected write operation, monitoring write data", UVM_HIGH)
                        apb_mitem.PWDATA_i = apb_mintf.cb_mntr.PWDATA_i;
                        apb_mitem.PSTRB_i = apb_mintf.cb_mntr.PSTRB_i;
                    end

                    @(apb_mintf.cb_mntr);
                    if (apb_mintf.cb_mntr.PENABLE_i) begin // Enable asserted
						`uvm_info(get_name(), "PENABLE asserted", UVM_HIGH)	
                        do begin
							`uvm_info(get_name(), "Waiting for PREADY to be asserted", UVM_HIGH)
                            if (apb_mintf.cb_mntr.PREADY_o) begin
                                if (apb_mitem.PWRITE_i == 0) begin // For read transfer
 									`uvm_info(get_name(), "Detected read operation, monitoring read data", UVM_HIGH)
                                    apb_mitem.PRDATA_o = apb_mintf.cb_mntr.PRDATA_o;
									apb_mitem.PSLVERR_o = apb_mintf.cb_mntr.PSLVERR_o;  
                        			apb_mitem.PSTRB_i = apb_mintf.cb_mntr.PSTRB_i;
                                end
                                end_time = $realtime;

								// writing log file
								if(apb_mntr_log) begin
									log_file_write();
								end
								apb_mntr_port.write(apb_mitem);	
								end_tr(apb_mitem);
								`uvm_info(get_name(), "Transaction Complete for Monitor!", UVM_NONE)
                                break;
                            end
                            @(apb_mintf.cb_mntr);
                        end while (1);
                    end else begin
                        `uvm_error(get_name(), "PENABLE is not high after one cycle of PSEL")
						apb_mitem.pt_err = 1; 
                    end
                end
            end
        end
    endtask

    // Close the log file at the end of simulation
    function void final_phase(uvm_phase phase);
        if (file_handle != 0)
            $fclose(file_handle);                           
    endfunction
endclass

class resetable_monitor extends  apb_monitor;
		`uvm_component_utils (resetable_monitor)

		uvm_event reset_on, reset_off; // any name can give

		function new (string name = "resetable_monitor", uvm_component parent = null);
			super.new(name,parent);
			`uvm_info(get_name(), "Inside resetable monitor!", UVM_NONE)		
		endfunction

		virtual function void build_phase (uvm_phase phase);
			super.build_phase(phase);

			reset_on  = uvm_event_pool::get_global("reset_asserted");
			reset_off = uvm_event_pool::get_global("reset_deasserted");

		endfunction

		virtual task run_phase (uvm_phase phase);
			fork
				begin : reset_check
					forever begin
						wait (apb_mintf.PRESETn_i == 0);
							reset_on.trigger();
							`uvm_info(get_name(), "Reset asseerted!", UVM_HIGH)
							disable monitoring;
							wait (apb_mintf.PRESETn_i == 1);
							reset_off.trigger();
							`uvm_info(get_name(), "Reset de-asseerted!", UVM_HIGH)
						end
				end
				begin : monitor_run
					forever begin
						@(apb_mintf.cb_mntr);
						if (apb_mintf.PRESETn_i == 1)
							monitoring();
						end
					end
			join_none
		endtask

		virtual task monitoring();
			`uvm_info (get_name(), "INside monitoring task", UVM_NONE)

            //@(apb_mintf.cb_mntr);
			// tracing the start time of the transaction
            start_time = $realtime;
		
			//`uvm_info(get_name(), "Monitoring VALID APB signals", UVM_HIGH)
            if (apb_mintf.cb_mntr.PSEL_i) begin // Select asserted

               apb_mitem = apb_seq_item::type_id::create("apb_mitem");

			   if (apb_mintf.cb_mntr.PENABLE_i) begin
			   	`uvm_info(get_name(), "PENABLE High at the same cycle of PSEL high", UVM_NONE)
			   	apb_mitem.pt_err = 1;
			   end

			   `uvm_info(get_name(), "PSELECT asserted", UVM_HIGH)

			   ok = begin_tr(apb_mitem, "APB_MONITOR_PACKET");

               apb_mitem.PADDR_i = apb_mintf.cb_mntr.PADDR_i;
               apb_mitem.PWRITE_i = apb_mintf.cb_mntr.PWRITE_i;
               apb_mitem.PRESETn_i = apb_mintf.PRESETn_i;

               if (apb_mintf.cb_mntr.PWRITE_i) begin // For write Transfer
  			   	`uvm_info(get_name(), "Detected write operation, monitoring write data", UVM_HIGH)
                apb_mitem.PWDATA_i = apb_mintf.cb_mntr.PWDATA_i;
                apb_mitem.PSTRB_i = apb_mintf.cb_mntr.PSTRB_i;
               end

               @(apb_mintf.cb_mntr);
               if (apb_mintf.cb_mntr.PENABLE_i) begin // Enable asserted
			   	`uvm_info(get_name(), "PENABLE asserted", UVM_HIGH)	
                   do begin
			   		`uvm_info(get_name(), "Waiting for PREADY to be asserted", UVM_HIGH)
                       if (apb_mintf.cb_mntr.PREADY_o) begin
                           if (apb_mitem.PWRITE_i == 0) begin // For read transfer
 			   				`uvm_info(get_name(), "Detected read operation, monitoring read data", UVM_HIGH)
                            apb_mitem.PRDATA_o = apb_mintf.cb_mntr.PRDATA_o;
			   				apb_mitem.PSLVERR_o = apb_mintf.cb_mntr.PSLVERR_o;  
                   			apb_mitem.PSTRB_i = apb_mintf.cb_mntr.PSTRB_i;
                           end
                           end_time = $realtime;

			   			// writing log file
			   			if(apb_mntr_log) begin
			   				log_file_write();
			   			end
			   			apb_mntr_port.write(apb_mitem);	
			   			end_tr(apb_mitem);
			   			`uvm_info(get_name(), "Transaction Complete for Monitor!", UVM_NONE)
                           break;
                       end
                       @(apb_mintf.cb_mntr);
                   end while (1);
               end else begin
                   `uvm_info(get_name(), "PENABLE is not high after one cycle of PSEL", UVM_NONE)
			   		apb_mitem.pt_err = 1; 
               end
            end
		endtask

endclass

