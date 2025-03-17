class scoreboard extends uvm_scoreboard;
	`uvm_component_utils (scoreboard)

	uvm_analysis_imp #(apb_seq_item, scoreboard) mntr2scb_impport;
	
	apb_seq_item read_trans[$];

	apb_seq_item rcvd_item, mtch_item;

	uvm_event reset_assert, reset_deassert;

	logic [31:0] data_memory [logic [31:0]];

	function new (string name = "scoreboard", uvm_component parent = null);
			super.new(name,parent);
	endfunction

	virtual function void write(apb_seq_item recevied_item);
		rcvd_item = apb_seq_item::type_id::create("rcvd_item");
		$cast(rcvd_item, recevied_item);

		if (rcvd_item.PSLVERR_o) begin
			slave_error(rcvd_item);	
		end else if(rcvd_item.pt_err) begin
			protocol_error(rcvd_item);
		end else if(rcvd_item.PWRITE_i) begin
			memory_write(rcvd_item);
		end else
			memory_read(rcvd_item);
	endfunction

	virtual function void slave_error(apb_seq_item err_item);
		if (!err_item.PWRITE_i && err_item.PSTRB_i != 0) begin
        	`uvm_info(get_name(), "Read Error! PSTRB_i non-zero! ", UVM_NONE)
        end	
	endfunction

   virtual function void memory_write(apb_seq_item wr_item);
        bit [31:0] existing_data, new_data, final_data;

        existing_data = data_memory[wr_item.PADDR_i];
        new_data      =  wr_item.PWDATA_i;

        for (int i = 0; i < `BYTE_LANE; i++) begin
                if (wr_item.PSTRB_i[i])
                        existing_data [(8*i+8)-1 -: 8] = 8'b00;
        end

        for (int i = 0; i < `BYTE_LANE; i++) begin
                if (!wr_item.PSTRB_i[i])
                        new_data [(8*i+8)-1 -: 8] = 8'b00;
        end

        final_data = existing_data | new_data; 

        data_memory[wr_item.PADDR_i] = final_data;
        	
		`uvm_info(get_name(), "Write transaction completed!", UVM_HIGH)
    endfunction

	virtual function void memory_read(apb_seq_item rd_item);
		if(data_memory.exists(rd_item.PADDR_i)) begin
			read_trans.push_back(rd_item);	
		end else begin
			`uvm_warning(get_type_name(), "Read in an empty Adress!")	
		end
	endfunction

	virtual function void build_phase (uvm_phase phase);
		super.build_phase(phase);
		mntr2scb_impport = new("mntr2scb_impport", this);

		reset_assert  = uvm_event_pool::get_global("reset_asserted");
		reset_deassert = uvm_event_pool::get_global("reset_deasserted");

	endfunction

	virtual task run_phase (uvm_phase phase);
		fork
			begin : reset_work
				forever begin
					reset_assert.wait_trigger();
					`uvm_info(get_name(), "Reset asseerted!", UVM_NONE)
					disable data_match;
					data_memory.delete();
					read_trans.delete();
					reset_deassert.wait_trigger();
					`uvm_info(get_name(), "Reset de-asseerted!", UVM_NONE)
				end
			end
			begin : scb_work
				forever begin
					data_match();
				end
			end
		join_none
	endtask

	virtual function protocol_error(apb_seq_item err_item);
		if(rcvd_item.PWRITE_i) begin
			`uvm_info(get_name(), "Protocol Violation for Write operation", UVM_NONE);
			memory_write(err_item);
		end else begin
			`uvm_info(get_name(), "Protocol Violation for Read operation", UVM_NONE);
			memory_read(err_item);
		end
	endfunction

	virtual task data_match();
		//`uvm_info(get_name(), "Start of data match", UVM_LOW);
	    wait(read_trans.size() > 0);
		mtch_item = apb_seq_item::type_id::create("mtch_item");
		mtch_item = read_trans.pop_front();
		if (mtch_item.PRDATA_o == data_memory[mtch_item.PADDR_i])
			`uvm_info(get_type_name(), "Tranasction data matched", UVM_NONE)
		else
			`uvm_error(get_type_name(), $sformatf("Data mismatched, Expected data = %0h, On address %0h Received data = %0h", data_memory[mtch_item.PADDR_i], mtch_item.PADDR_i, mtch_item.PRDATA_o))
			
		//`uvm_info(get_name(), "End of data match", UVM_LOW);
	endtask

	virtual function void check_phase(uvm_phase phase);
		if(!read_trans.size()) begin
			`uvm_info(get_type_name(), "Read queue is empty!", UVM_HIGH)
		end else begin
			`uvm_error(get_type_name()," Readqueue is not empty!")
		end
	endfunction

endclass

