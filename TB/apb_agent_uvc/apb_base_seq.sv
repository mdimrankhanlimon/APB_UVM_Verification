class apb_base_seq extends uvm_sequence();
		bit [`ADDR-1:0] addr;
		bit 			op;            // op -->1 write, op =0 -->read
		bit [`DATA_WIDTH-1:0] data;
		bit [`BYTE_LANE-1:0] strb;

		// Methods

		// Constructor
		function new(string name="apb_base_seq")
			super.new(name);
		endfunction

		// body task
		virtual task body();
			`uvm_info(get_name(),$formatf("Running Base Sequeence From base Sequence"),UVM_HIGH);
		endtask

endclass

class apb_write_seq extends apb_base_seq;
		`uvm_object_utils (apb_write_srq);

		// constructor
		function new("string name = "apb_write_srq");
		endfucntion
endclass
