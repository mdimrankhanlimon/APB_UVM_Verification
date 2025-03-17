
class apb_driver extends uvm_driver #(apb_seq_item);
	`uvm_component_utils(apb_driver)
	`uvm_register_cb(apb_driver, apb_driver_callback)

	virtual apb_interface apb_dintf;

	apb_seq_item item_obj;

	int okey;

	// Internal variable to assign delay and reset
	int DEL;
	bit RANDOM_RESET;

	function new (string name = "apb_driver", uvm_component parent = null);
			super.new(name, parent);
			// Value of delay passing from command line
			if(!$value$plusargs("DEL=%d", DEL)) begin
				`uvm_warning("Delay is not set", UVM_NONE)
			end
			if(!$value$plusargs("RANDOM_RESET=%b", RANDOM_RESET)) begin
				`uvm_warning("RANDOM RESET is not Activated", UVM_NONE)
			end
	endfunction

	virtual function void build_phase(uvm_phase phase);
		super.build_phase(phase);
		
		 if(! uvm_config_db #(virtual apb_interface)::get (this,"*","APB_INTF", apb_dintf))
				 `uvm_error (get_full_name(), "Could get apb interface from driver")

	endfunction



	virtual task delay_assign(virtual apb_interface intf);
		//repeat($urandom_range(0,10))
			@(negedge intf.PCLK_i );  // example -1 cyecle delay
	endtask 

	virtual task sel_enb_chage(virtual apb_interface intf);
		// Assigning delay before transactions
		repeat($urandom_range(0, DEL)) begin
			@(negedge intf.PCLK_i ); 
			`uvm_info(get_name(), "inside sel_enb delay", UVM_HIGH)
		end
		intf.cb_drvr.PSEL_i  <= 1'b1;
		delay_assign(intf);
		intf.cb_drvr.PENABLE_i  <= 1'b1;
	endtask


	virtual task contr_signl_chng(apb_seq_item item, virtual apb_interface intf);
		intf.cb_drvr.PADDR_i  <= item.PADDR_i;
		intf.cb_drvr.PWRITE_i <= item.PWRITE_i;
		if (item.PWRITE_i) begin
			intf.cb_drvr.PWDATA_i <= item.PWDATA_i;
		end
		intf.cb_drvr.PSTRB_i  <= item.PSTRB_i;
	endtask



	virtual task drive(apb_seq_item item);
	
		int cycle_count = 0;

		okey = begin_tr(req, "APB_DRIVER_PACKET");

		@(apb_dintf.cb_drvr);
		fork
			sel_enb_chage(apb_dintf); 
			contr_signl_chng(req, apb_dintf);
		join
		do 
		begin
				@(posedge apb_dintf.PCLK_i);
				if (apb_dintf.PREADY_o)
				begin
					`uvm_info(get_name(), "PREADY received from Interface", UVM_HIGH)
		 			apb_dintf.cb_drvr.PSEL_i  <= 1'b0;
		 			apb_dintf.cb_drvr.PENABLE_i  <= 1'b0;
					break;
				end

				cycle_count ++;
				if (cycle_count > 20) begin
						`uvm_error (get_name(), "Didn't get PREADY high more than 20 cycle")
                        break;
                end
		end while (1);
		`uvm_info(get_name(), "Transfer complete", UVM_HIGH)
		end_tr(req);

	endtask

	task reset_intf();
		`uvm_do_callbacks(apb_driver, apb_driver_callback, reset_intf(apb_dintf))
		`uvm_info(get_name(), "Driving reset", UVM_HIGH)
		apb_dintf.PRESETn_i <=0;
    	apb_dintf.PADDR_i   <=0;
    	apb_dintf.PWRITE_i  <=0;
    	apb_dintf.PWDATA_i  <=0;
    	apb_dintf.PSTRB_i   <=0;
    	apb_dintf.PSEL_i    <=0;
    	apb_dintf.PENABLE_i <=0;
		
		`uvm_info(get_name(), "Waiting for reset deassertion", UVM_HIGH)
		@(posedge apb_dintf.PCLK_i);
		apb_dintf.PRESETn_i <=1;
		`uvm_info(get_name(), "Reset Complete", UVM_HIGH)
	endtask


	virtual task run_phase(uvm_phase phase);
		forever begin
			`uvm_info(get_name(), "Waiting for sequence item from sequencer", UVM_HIGH)
			seq_item_port.get_next_item(req);
			`uvm_info(get_name(), "Received Item from Sequencer", UVM_HIGH)
			if (!req.PRESETn_i)
			begin
					`uvm_info(get_name(), "Reset sequence detected by driver", UVM_NONE)
					reset_intf();
					`uvm_info(get_name(), "Reset completed", UVM_NONE)
			end
			else begin
					`uvm_info(get_name(), "Driving regular sequence", UVM_HIGH)
					drive(req);
					`uvm_info(get_name(), "Driving regular sequence comepleted", UVM_HIGH)
			end
			
			if(RANDOM_RESET) begin		
				if(!req.RESET) reset_intf;
			end

			`uvm_info(get_name(), "Sequence item driving done", UVM_HIGH)
			seq_item_port.item_done();
		end
	endtask


endclass

// 1. sel-enb delay
class sel_enb_error_drive extends apb_driver;
		`uvm_component_utils(sel_enb_error_drive)

		function new (string name = "sel_enb_error_drive", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task delay_assign(virtual apb_interface intf);
			repeat($urandom_range(0,10))
				@(posedge intf.PCLK_i );  // example -1 cyecle delay
		endtask 
endclass

// 2. sel_enb_high together
class sel_enb_high_drive extends apb_driver;
		`uvm_component_utils(sel_enb_high_drive)

		function new (string name = "sel_enb_error_drive", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task sel_enb_chage(virtual apb_interface intf);
			intf.cb_drvr.PSEL_i  <= 1'b1;
			intf.cb_drvr.PENABLE_i  <= 1'b1;
		endtask
endclass

// 3. enb_high_before_sel_drive
class enb_high_bef_sel_drive extends apb_driver;
		`uvm_component_utils(enb_high_bef_sel_drive)

		function new (string name = "sel_enb_error_drive", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task delay_assign(virtual apb_interface intf);
			repeat($urandom_range(0,10))
				@(posedge intf.PCLK_i );  // example -1 cyecle delay
		endtask 

		virtual task sel_enb_chage(virtual apb_interface intf);
			intf.cb_drvr.PENABLE_i  <= 1'b1;
			delay_assign(intf);
			intf.cb_drvr.PSEL_i  <= 1'b1;
		endtask
endclass

// 4. enb high change ctrl signal
class enb_high_change_ctrl_drive extends apb_driver;
		`uvm_component_utils(enb_high_change_ctrl_drive)

		function new (string name = "sel_enb_error_drive", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task delay_assign(virtual apb_interface intf);
			@(posedge intf.PCLK_i );  // example -1 cyecle delay
		endtask 

		virtual task contr_signl_chng(apb_seq_item item, virtual apb_interface intf);
			intf.cb_drvr.PADDR_i  <= item.PADDR_i;
			intf.cb_drvr.PWRITE_i <= item.PWRITE_i;
			if (item.PWRITE_i) begin
				intf.cb_drvr.PWDATA_i <= item.PWDATA_i;
			end
			intf.cb_drvr.PSTRB_i  <= item.PSTRB_i;

			delay_assign(intf);
			intf.cb_drvr.PADDR_i  <= $random;
	        intf.cb_drvr.PWRITE_i <= $random;
    	    if (item.PWRITE_i) begin
        	    intf.cb_drvr.PWDATA_i <= $random;
	        end
    	    intf.cb_drvr.PSTRB_i  <= $random;	
		endtask
endclass

// 5. enb_low_before_pready_drive
class enb_low_before_pready_drive extends apb_driver;
		`uvm_component_utils(enb_low_before_pready_drive)

		function new (string name = "sel_enb_error_drive", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task delay_assign(virtual apb_interface intf);
			repeat($urandom_range(0,10))
				@(posedge intf.PCLK_i );  // example -1 cyecle delay
		endtask 

		virtual task sel_enb_chage(virtual apb_interface intf);
			intf.cb_drvr.PSEL_i  <= 1'b1;
			delay_assign(intf);
			intf.cb_drvr.PENABLE_i  <= 1'b1;
			delay_assign(intf);
			intf.cb_drvr.PENABLE_i  <= 1'b0;
		endtask
endclass
