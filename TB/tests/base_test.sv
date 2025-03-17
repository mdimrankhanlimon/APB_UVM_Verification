`define APB_SQCR env.apb_agnt.apb_sqcr

class base_test extends uvm_test;
	`uvm_component_utils(base_test)

	// Fields
	environment env;
	environment_config   env_cfg;

	//uvm_factory factory = uvm_factory::get();
	uvm_factory factory;
	uvm_coreservice_t cs = uvm_coreservice_t::get();

	//Constructor
	function new (string name = "base_test", uvm_component parent = null);
			super.new(name, parent);
	endfunction

	virtual function void apb_build_config (
			environment_config   env_cfg_hndl,
			uvm_active_passive_enum agent_activation = UVM_PASSIVE,
			bit agent_cover = 1
	);

		env_cfg_hndl.apb_agent_stat = agent_activation;
		env_cfg_hndl.apb_agent_cover = agent_cover;
	endfunction

	//Phase
	virtual function void build_phase (uvm_phase phase);
		super.build_phase(phase);
		`uvm_info(get_name(), "build phase ", UVM_NONE)

		set_config_int("*", "recording_detail", UVM_FULL);
		env_cfg = environment_config::type_id::create("env_cfg");

		apb_build_config(env_cfg, UVM_ACTIVE, 1);
		env_cfg.has_scb = 1;
		env_cfg.apb_mntr_log = 1;
		`uvm_info(get_name(), $sformatf("value of mntr_log: %0d", env_cfg.apb_mntr_log), UVM_NONE);

		uvm_config_db #(environment_config)::set(null, "*", "ENV_CFG",env_cfg);

		set_type_override_by_type(apb_monitor::get_type(), resetable_monitor::get_type());

		// type override --> inside whole tb env all instance override
		// inst override --> for particular override

		//source object , destination object // Will pass from command line
		//set_type_override_by_type(apb_driver::get_type(), sel_enb_error_drive::get_type());
		
		env = environment::type_id::create("env", this);

	endfunction

	function void end_of_elaboration_phase (uvm_phase phase);
			super.end_of_elaboration_phase(phase);
			this.print();
			factory = cs.get_factory();
			factory.print();
	endfunction

	virtual task run_phase(uvm_phase phase);
		super.run_phase(phase);
		`uvm_info(get_name(), "Running Base Test", UVM_NONE)
	endtask

	/* TODO :: Later will implement
	virtual task arb_change;
		// env.agent.seqr.set_arbitration(UVM_SEQ_ARB_WEIGHTED)
		`uvm_info(get_name(), $sformatf ("Arbitration method = %s",env.agent.seqr.get_arbitration()))
	endtask
	*/
   virtual function void report_phase(uvm_phase phase);
   	uvm_report_server svr;
	super.report_phase(phase);

	svr = uvm_report_server::get_server();
	if (svr.get_severity_count(UVM_FATAL) + svr.get_severity_count(UVM_ERROR) > 0 ) begin
		$display("---------------------------------------------------------------");
		$display("---------------    TEST FAIL    -------------------------------");
		$display("---------------------------------------------------------------");

	end else begin
		$display("---------------------------------------------------------------");
		$display("---------------    TEST PASS    -------------------------------");
		$display("---------------------------------------------------------------");
	end

   endfunction	

endclass


class error_base_test extends base_test;
	`uvm_component_utils(error_base_test)

	function new(string name= "error_base_test", uvm_component parent = null);
			super.new(name,parent);
	endfunction

	//Phase
	virtual function void build_phase (uvm_phase phase);
		super.build_phase(phase);
		// env_cfg = environment_config::type_id::create("env_cfg");
		
		// apb_build_config(env_cfg, UVM_ACTIVE, 0);
		// env_cfg.has_scb = 0;
		
		// uvm_config_db #(environment_config)::set(null, "*", "ENV_CFG",env_cfg);

		// set_type_override_by_type(apb_driver::get_type(), sel_enb_error_drive::get_type());
		
	    //	env = environment::type_id::create("env", this);

	endfunction

	virtual function void start_of_simulation_phase (uvm_phase phase);
		env.apb_agnt.apb_mntr.set_report_severity_id_override(UVM_FATAL, "apb_mntr", UVM_WARNING);
		env.apb_agnt.apb_mntr.set_report_severity_id_override(UVM_ERROR, "apb_mntr", UVM_WARNING);
		env.apb_agnt.apb_drvr.set_report_severity_id_override(UVM_FATAL, "apb_drvr", UVM_WARNING);
		env.apb_agnt.apb_drvr.set_report_severity_id_override(UVM_ERROR, "apb_drvr", UVM_WARNING);
	endfunction
	
endclass

