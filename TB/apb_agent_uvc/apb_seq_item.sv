class apb_seq_item extends uvm_sequence_item;

		// field 
    	rand bit                 	 PRESETn_i;
		rand bit   [`ADDR_WIDTH-1:0] PADDR_i;
		rand bit                     PWRITE_i;
		rand bit   [`DATA_WIDTH-1:0] PWDATA_i;
		rand bit   [`BYTE_LANE-1:0]  PSTRB_i;
		rand bit                     PSEL_i;
		rand bit                     PENABLE_i;
		
		bit   [`DATA_WIDTH-1:0] 	 PRDATA_o;
		bit                     	 PREADY_o;
		bit                     	 PSLVERR_o;
		int 						 item_count;
		bit 						 pt_err;	

		// variable to randomize reset
        rand bit RESET;

		// factory registration
		`uvm_object_utils_begin(apb_seq_item)
			`uvm_field_int (PRESETn_i, UVM_ALL_ON | UVM_NORECORD)
			`uvm_field_int (PADDR_i, UVM_ALL_ON |  UVM_DEC)
			`uvm_field_int (PWRITE_i, UVM_ALL_ON)
			`uvm_field_int (PWDATA_i, UVM_ALL_ON | UVM_HEX)
			`uvm_field_int (PSTRB_i, UVM_ALL_ON)
			`uvm_field_int (PSEL_i, UVM_ALL_ON | UVM_NORECORD)
			`uvm_field_int (PENABLE_i, UVM_ALL_ON | UVM_NORECORD)
			`uvm_field_int (RESET, UVM_ALL_ON | UVM_NORECORD)
			`uvm_field_int (pt_err, UVM_ALL_ON | UVM_NORECORD)

			`uvm_field_int (PRDATA_o, UVM_ALL_ON | UVM_HEX)
			`uvm_field_int (PREADY_o, UVM_ALL_ON | UVM_NORECORD)
			`uvm_field_int (PSLVERR_o, UVM_ALL_ON)
		`uvm_object_utils_end
		
		// constructor
		function new (string name = "apb_seq_item");
			super.new(name);
		endfunction

		// constraints for random reset
        constraint reset {
            RESET dist {'b0 := 2, 'b1 := 98};
        }
		constraint address {
				PADDR_i % 4 == 0;
		}
		
endclass

class apb_valid_addr_item extends apb_seq_item;

	`uvm_object_utils (apb_valid_addr_item)

	function new (string name = "apb_valid_addr_item");
			super.new(name);
	endfunction

	constraint valid_addr {
		PADDR_i < 'd1024; 
	}

endclass

