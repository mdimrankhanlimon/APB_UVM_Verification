
class apb_sequencer extends uvm_sequencer #(apb_seq_item);
		`uvm_component_utils(apb_sequencer)

		function new (string name = "apb_sequencer", uvm_component parent = null);
				super.new(name,parent);
		endfunction



endclass

/****************************
ARB_FIFO
ARB_WEIGHTED
ARB_RANDOM
STRIC_FIFO
STRICT_RANDOM
ARB_USER
****************************/


