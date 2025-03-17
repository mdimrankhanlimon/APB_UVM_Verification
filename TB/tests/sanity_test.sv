class sanity_test extends base_test;
		`uvm_component_utils(sanity_test)

		apb_write_seq write_seq;
		apb_read_seq  read_seq;
		apb_reset_seq  rst_seq;
		
		function new (string name = "sanity_test", uvm_component parent = null);
				super.new(name, parent);
		endfunction

	virtual task run_phase(uvm_phase phase);
		super.run_phase(phase);
		phase.raise_objection (this);
		`uvm_info(get_name(), $sformatf("at time = %0t,  Running sanity_test", $time()), UVM_NONE)
		rst_seq = apb_reset_seq::type_id::create("rst_seq");
		write_seq = apb_write_seq::type_id::create("write_seq");
		read_seq = apb_read_seq::type_id::create("read_seq");

		rst_seq.start(`APB_SQCR);
		#20ns;
		write_seq.start(`APB_SQCR);
		#20ns;
		read_seq.start(`APB_SQCR);
		
		phase.drop_objection(this);

		`uvm_info(get_name(), $sformatf("at time = %0t Finish sanity_test", $time()), UVM_NONE)
	endtask

endclass
