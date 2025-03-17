
class environment_config extends uvm_object;
		`uvm_object_utils (environment_config)

		uvm_active_passive_enum apb_agent_stat = UVM_PASSIVE;
		uvm_active_passive_enum apb_agent_stat_1 = UVM_PASSIVE;
		uvm_active_passive_enum apb_agent_stat_2 = UVM_PASSIVE;
		uvm_active_passive_enum apb_agent_stat_3 = UVM_PASSIVE;

		bit apb_agent_cover = 0;
		bit apb_agent_cover_1 = 0;
		bit apb_agent_cover_2 = 0;
		bit apb_agent_cover_3 = 0;

		bit has_scb = 1;

		bit apb_mntr_log;

		function new (string name = "environment_config");
				super.new(name);
		endfunction


endclass
