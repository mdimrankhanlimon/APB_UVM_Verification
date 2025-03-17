
class reset_test extends base_test;
		`uvm_component_utils (reset_test)

	    reset_seq seq;	
		apb_reset_seq rst_seq;

		function new(string name= "reset_test", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual function void build_phase (uvm_phase phase);
				
			`uvm_info(get_name(), "build phase ", UVM_NONE)
			env_cfg = environment_config::type_id::create("env_cfg");
			
			apb_build_config(env_cfg, UVM_ACTIVE, 0);
			env_cfg.has_scb = 0;
			env_cfg.apb_mntr_log = 1;

			uvm_config_db #(environment_config)::set(null, "*", "ENV_CFG",env_cfg);
			set_type_override_by_type(apb_driver_callback::get_type(), reset_callback::get_type());
			env = environment::type_id::create("env", this);
		endfunction

		virtual task run_phase(uvm_phase phase);
			phase.phase_done.set_drain_time(this, 50ns);

			phase.raise_objection(this);
				rst_seq = apb_reset_seq::type_id::create("rst_seq");
				rst_seq.start(`APB_SQCR);
			 	uvm_callbacks#(apb_driver,apb_driver_callback)::add(env.apb_agnt.apb_drvr, env.apb_agnt.drvr_cb);
				repeat(50) begin
					seq = reset_seq::type_id::create("seq");
					seq.start(`APB_SQCR);
				end
			phase.drop_objection(this);
		endtask

endclass



