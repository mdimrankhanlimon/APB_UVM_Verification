
class cont_wr_rd_test extends base_test;
		`uvm_component_utils (cont_wr_rd_test)

		cont_wr_rd_knobs_seq  seq;
		
		function new(string name= "cont_wr_rd_test", uvm_component parent = null);
				super.new(name,parent);
		endfunction


		virtual task run_phase(uvm_phase phase);
			phase.phase_done.set_drain_time(this, 40ns);
			
			phase.raise_objection(this);
				seq = cont_wr_rd_knobs_seq::type_id::create("seq");
				seq.start(`APB_SQCR);
			phase.drop_objection(this);
		endtask



endclass



