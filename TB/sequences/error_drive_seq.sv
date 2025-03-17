
class error_drive_seq extends apb_base_seq;
    `uvm_object_utils(error_drive_seq)

    apb_seq_item item;

    function new(string name = "error_drive_seq");
        super.new(name);
    endfunction

    virtual task body();
        `uvm_info(get_name(), $sformatf("Start >>>> %s", get_type_name()),UVM_NONE)
        item = apb_seq_item::type_id::create("item");
		start_item(item);
		item.PRESETn_i = 1;
  		item.PADDR_i = $random;
        item.PWRITE_i = $urandom_range(0,1);
 		item.PWDATA_i = $random;
   		item.PSTRB_i = $urandom_range(4'b0000,4'b1111);
        item.PSEL_i = 1;
        item.PENABLE_i = 1; 
		finish_item(item);
        `uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)
    endtask
endclass

