
class sanity_simple_test extends base_test;
		`uvm_component_utils (sanity_simple_test)

		sanity_simple_seq  seq;
		
		function new(string name= "sanity_simple_test", uvm_component parent = null);
				super.new(name,parent);
		endfunction


		virtual task run_phase(uvm_phase phase);
			phase.phase_done.set_drain_time(this, 40ns);
			
			phase.raise_objection(this);
			repeat (10) begin
				seq = sanity_simple_seq::type_id::create("seq");
				seq.start(`APB_SQCR);
			end
			phase.drop_objection(this);
		endtask



endclass



