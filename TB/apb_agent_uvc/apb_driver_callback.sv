
typedef class apb_driver;

class apb_driver_callback extends uvm_callback;
		`uvm_object_utils(apb_driver_callback)

		function new(string name = "apb_driver_callback");
				super.new(name);
		endfunction
	
		virtual task reset_intf(virtual apb_interface apb_cintf); 
		endtask

endclass

class reset_callback extends apb_driver_callback;
		`uvm_object_utils(reset_callback)

		function new(string name = "reset_callback");
				super.new(name);
		endfunction

		virtual task reset_intf(virtual apb_interface apb_cintf);
			`uvm_info(get_name(), "Driving reset callback", UVM_NONE)

			apb_cintf.PRESETn_i <= 0;
    		apb_cintf.PADDR_i   <= 0;
    		apb_cintf.PWRITE_i  <= 0;
    		apb_cintf.PWDATA_i  <= 0;
    		apb_cintf.PSTRB_i   <= 0;
    		apb_cintf.PSEL_i    <= 0;
    		apb_cintf.PENABLE_i <= 0;
			
			`uvm_info(get_name(), "Waiting for reset deassertion from driver_callback", UVM_NONE)

			repeat($urandom_range(1,10)) @(posedge apb_cintf.PCLK_i);

			apb_cintf.PRESETn_i <=1;

			`uvm_info(get_name(), "Reset Complete from driver_callback", UVM_NONE)
        endtask

endclass
