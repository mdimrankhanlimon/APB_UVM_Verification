
class environment extends uvm_env;
		`uvm_component_utils(environment)

		environment_config   env_cfg;

		apb_agent apb_agnt;
		apb_agent_config 	apb_agnt_cfg;
		scoreboard scb;

		function new (string name = "environment", uvm_component parent = null);
				super.new(name,parent);
		endfunction

		virtual function void build_phase(uvm_phase phase);
				if (! uvm_config_db #(environment_config)::get(this, "*", "ENV_CFG", env_cfg) )
						`uvm_fatal(get_name(), "Could not get env configuration from environment class")

				apb_agnt_cfg = apb_agent_config::type_id::create("apb_agnt_cfg");
				apb_agnt_cfg.is_active = env_cfg.apb_agent_stat;
				apb_agnt_cfg.has_cover = env_cfg.apb_agent_cover;
				apb_agnt_cfg.apb_mntr_log = env_cfg.apb_mntr_log;
				`uvm_info(get_name(), $sformatf("value of mntr_log: %0d", apb_agnt_cfg.apb_mntr_log), UVM_NONE);

				uvm_config_db #(apb_agent_config)::set(null, "*", "APB_AGNT_CFG", apb_agnt_cfg);

				apb_agnt = apb_agent::type_id::create("apb_agnt", this);

				if (env_cfg.has_scb)
						scb = scoreboard::type_id::create("scb", this);


		endfunction

		virtual function void connect_phase(uvm_phase phase);
			if (env_cfg.has_scb)
					apb_agnt.apb_agnt_port.connect(scb.mntr2scb_impport);

		endfunction

endclass

