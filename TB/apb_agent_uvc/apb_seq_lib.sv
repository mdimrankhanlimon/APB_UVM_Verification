`define SEQ_SP	`uvm_info (get_name(), $sformatf("Start  >>> %s ", get_type_name()), UVM_NONE)
`define SEQ_EP	`uvm_info (get_name(), $sformatf("End  >>> %s ", get_type_name()), UVM_NONE)


class apb_base_seq extends uvm_sequence #(apb_seq_item);

		// Fields
		bit [`ADDR_WIDTH-1:0] addr;
		bit                   op; // op=1--> write, op=0--> read
		bit [`DATA_WIDTH-1:0] data;
		bit [`BYTE_LANE-1:0]  strb;

		// Methods


		//Factory registration
		`uvm_object_utils (apb_base_seq)


		//Constructor
		function new (string name = "apb_base_seq");
				super.new(name);
		endfunction

		// body task
		virtual task body();
			`uvm_info (get_name(), $sformatf("Running Base sequence From base Seq"), UVM_HIGH);
		endtask

endclass


class apb_write_seq extends apb_base_seq;
	`uvm_object_utils (apb_write_seq)

		apb_seq_item item;
	
		//Constructor
		function new (string name = "apb_write_seq");
				super.new(name);
		endfunction


		// body task


		virtual task body();
			`SEQ_SP
			`uvm_do_with (req, {req.PWRITE_i == 1; req.PRESETn_i==1; req.PSTRB_i != 0;})
			//req.print();
			`SEQ_EP
		endtask

endclass


class apb_read_seq extends apb_base_seq;
	`uvm_object_utils (apb_read_seq)

		apb_seq_item item;
	
		//Constructor
		function new (string name = "apb_read_seq");
				super.new(name);
		endfunction


		// body task

		virtual task body();
			`SEQ_SP
			`uvm_do_with (req, {req.PWRITE_i == 0; req.PRESETn_i==1; req.PSTRB_i==0;})
			//req.print();
			`SEQ_EP
		endtask

endclass


class apb_reset_seq extends apb_base_seq;
	`uvm_object_utils (apb_reset_seq)

		apb_seq_item item;
	
		//Constructor
		function new (string name = "apb_reset_seq");
				super.new(name);
		endfunction


		// body task

		virtual task body();
			`SEQ_SP
			//lock(m_sequencer);
			`uvm_do_with (req, {req.PWRITE_i == 1; req.PRESETn_i==0;})
			//req.print();
			//unlock(m_sequencer);
			`SEQ_EP
		endtask

endclass

class apb_rand_seq extends apb_base_seq;
	`uvm_object_utils (apb_rand_seq)

		apb_seq_item item;
	
		//Constructor
		function new (string name = "apb_rand_seq");
				super.new(name);
		endfunction


		// body task

		virtual task body();
			`SEQ_SP
			`uvm_do_with (req, { req.PRESETn_i==1;})
			req.print();
			`SEQ_EP
		endtask

endclass

class apb_directed_seq extends apb_base_seq;
		`uvm_object_utils (apb_directed_seq)

		function new (string name = "apb_directed_seq");
				super.new(name);
		endfunction

		virtual task body();
			`SEQ_SP
			`uvm_do_with (req, { req.PRESETn_i==1;
								 req.PADDR_i  == local::addr;
								 req.PWRITE_i == local::op;
								 req.PWDATA_i == local::data;
								 req.PSTRB_i  == local::strb;
			})
			//req.print();
			`SEQ_EP
	endtask

endclass



class apb_directed_seq_mod1 extends apb_base_seq;
		`uvm_object_utils (apb_directed_seq)

		function new (string name = "apb_directed_seq");
				super.new(name);
		endfunction

		virtual task body();
			`uvm_info (get_full_name(), $sformatf("Running %s sequence", get_name()), UVM_NONE)
			req = apb_seq_item::type_id::create("req");
			start_item(req);
			// or wait_for_grant();
			assert (req.randomize() with { req.PRESETn_i==1;
								 req.PADDR_i  == local::addr;
								 req.PWRITE_i == local::op;
								 req.PWDATA_i == local::data;
								 req.PSTRB_i  == local::strb;
			});
			finish_item(req);
			// or
			//send_request(req);
			//wait_for_item_done(); 
			//get_response(rsp);
	endtask

endclass






/******************************************************************
1) creation --> create 
2) sync ---> stat_item() for step 2 &3
3) pro_do_hook
4) randomization --> .randomize()
5) mid_hook
6) req send + wait 4 resp --> finish_item()
7) post_hook




`uvm_do (req)
`uvm_do_with(req, {})

`uvm_create(req)
`uvm_rand_send()
`uvm_rand_send_with()

`uvm_do_on()
`uvm_do_with_on()

******************************************************************/
/*
uvm_sequence_library
handshake method done

-------------------------
seq_1
seq_2
seq-3
seq_4
Seq_5
---------------------------


lock, unlock
grab, ungrab



seq_1 --> running 
out <-- interrupt gen
seq_3 (interrupt service sequce) --> seq_3 if lock sequene

multipy 100 200 out_reg [64 clock cycle]
after 5 cycle interuppt [uart interrpt]

kill()
is_blocked()
has_locked()


seq_2 -->  waiting for run


******************************************************************/

