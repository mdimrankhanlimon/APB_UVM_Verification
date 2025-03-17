
class apb_agent extends uvm_agent;
		`uvm_component_utils (apb_agent)


		apb_agent_config 	apb_agnt_cfg;
		apb_sequencer 		apb_sqcr;
		apb_driver  		apb_drvr;
		apb_monitor 		apb_mntr;
		apb_driver_callback drvr_cb;
		apb_coverage 		apb_cov;

		uvm_analysis_port #(apb_seq_item) apb_agnt_port;


		function new (string name = "apb_agent", uvm_component parent = null);
				super.new(name,parent);
		endfunction


		virtual function void build_phase (uvm_phase phase);
			if (! uvm_config_db #(apb_agent_config)::get(this, "*", "APB_AGNT_CFG", apb_agnt_cfg) )
					`uvm_fatal(get_name(), "Could not get agent configuration from apb_agent class")

			if (apb_agnt_cfg.is_active == UVM_ACTIVE) begin
					apb_sqcr = apb_sequencer::type_id::create("apb_sqcr", this);
					apb_drvr = apb_driver::type_id::create("apb_drvr", this);
			 		drvr_cb = apb_driver_callback::type_id::create("drvr_cb");
			end
			`uvm_info(get_type_name(), "Before coverage Instace creating from Agent", UVM_NONE)
			if (apb_agnt_cfg.has_cover) begin
				`uvm_info(get_type_name(), "Coverage Instace creating from Agent", UVM_NONE)
				apb_cov = apb_coverage::type_id::create("apb_cov", this);
			end

			apb_mntr = apb_monitor::type_id::create("apb_mntr", this);

			apb_agnt_port = new("apb_agnt_port", this);

			apb_mntr.apb_mntr_log = apb_agnt_cfg.apb_mntr_log;
			`uvm_info(get_name(), $sformatf("value of mntr_log: %0d", apb_mntr.apb_mntr_log), UVM_NONE);

		endfunction


		virtual function void connect_phase (uvm_phase phase);
			
			if (apb_agnt_cfg.is_active == UVM_ACTIVE) begin
					apb_drvr.seq_item_port.connect(apb_sqcr.seq_item_export);
			end
			
			apb_mntr.apb_mntr_port.connect(apb_agnt_port);


			if (apb_agnt_cfg.has_cover) begin
				apb_mntr.apb_mntr_port.connect(apb_cov.analysis_export);
			end		
		endfunction

endclass



