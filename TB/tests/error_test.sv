
class error_test extends error_base_test;
		`uvm_component_utils (error_test)

	    apb_reset_seq apb_rst;	
		error_drive_seq error_drive;

		function new(string name= "error_test", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual task run_phase(uvm_phase phase);
			phase.phase_done.set_drain_time(this, 50ns);
			
			phase.raise_objection(this);
				apb_rst = apb_reset_seq::type_id::create("apb_rst");
				apb_rst.start(`APB_SQCR);
				repeat(100) begin
					error_drive = error_drive_seq::type_id::create("error_drive");
					error_drive.start(`APB_SQCR);
				end
			phase.drop_objection(this);
		endtask
endclass



