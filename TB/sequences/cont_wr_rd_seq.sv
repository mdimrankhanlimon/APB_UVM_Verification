class cont_wr_rd_seq extends apb_base_seq;
	`uvm_object_utils(cont_wr_rd_seq)

	apb_reset_seq apb_rst;
	apb_read_seq read_seq;
	apb_seq_item item;
	apb_write_seq write_seq;

	function new(string name = "cont_wr_rd_seq" );
		super.new(name);
	endfunction

	virtual task body();
		`uvm_info(get_name(), $sformatf("Start >>>> %s", get_type_name()),UVM_NONE)
		apb_rst = apb_reset_seq::type_id::create("apb_rst");
		apb_rst.start(m_sequencer,this);
    	`uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)
		#20ns;
		repeat(20) cont_wr_rd_seq();
	endtask

	virtual task cont_wr_rd_seq ();
		`uvm_info(get_name(), $sformatf("Start >>>> %s", get_type_name()),UVM_NONE)
		
		write_seq = apb_write_seq::type_id::create("write_seq");
		write_seq.start(m_sequencer,this);	

    	`uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)

		#20ns;

		`uvm_info(get_name(), $sformatf("Start >>>> %s", get_type_name()),UVM_NONE)

		read_seq = apb_read_seq::type_id::create("read_seq");
		read_seq.start(m_sequencer,this);

    	`uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)
	endtask
endclass
