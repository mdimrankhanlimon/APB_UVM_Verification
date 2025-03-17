
class sanity_simple_seq extends apb_base_seq;
		apb_reset_seq    apb_rst;
		apb_directed_seq apb_seq[2];

		bit [6:0] temp_addr;

		`uvm_object_utils(sanity_simple_seq)


		function new(string name = "sanity_simple_seq");
				super.new(name);
		endfunction


		virtual task body();
			`uvm_info (get_name(), $sformatf("Start  >>>  %s", get_type_name()), UVM_NONE)
			apb_rst = apb_reset_seq::type_id::create("apb_rst");
			apb_rst.start(m_sequencer, this);

			#20ns;
            temp_addr = $urandom_range(0, `DEPTH) & ~3; // Random address but word aligned
			
            apb_seq[0] = apb_directed_seq::type_id::create("apb_seq_write");
			apb_seq[0].addr = temp_addr;
			apb_seq[0].op   = 1'b1;
			apb_seq[0].data = $urandom;
			apb_seq[0].strb = 4'b1111;
			apb_seq[0].start(m_sequencer,this);

			#20ns;
			apb_seq[1] = apb_directed_seq::type_id::create("apb_seq_read");
			apb_seq[1].addr = temp_addr;
			apb_seq[1].op   = 1'b0;
			apb_seq[1].data = $urandom;
			apb_seq[1].strb = 4'b0000;
			apb_seq[1].start(m_sequencer,this);

			#20ns;
			`uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)
		endtask





endclass





