class cont_wr_rd_knobs_loc_seq extends apb_base_seq;

    // Factory Registration
    `uvm_object_utils (cont_wr_rd_knobs_loc_seq)

    // Properties
    apb_reset_seq      rst_seq;
    apb_directed_seq   wr_seq;
    apb_directed_seq   rd_seq;

    // Variables
    int unsigned WORD_KNOB;
    int unsigned HALF_WORD_KNOB;
    int unsigned BYTE_KNOB;
    rand int unsigned rand_val;
    rand bit [`BYTE_LANE-1:0]  temp_strb ;
    static bit [`ADDR_WIDTH-1:0] prev_addr;
    static bit [`ADDR_WIDTH-1:0] first_addr;
    int iter_count = `DEPTH/10;

    // Address Knobs
    string WR_ADDR;
    string RD_ADDR;
    string LOC;
   
    // Methods
    // Address generation method
    function bit [`ADDR_WIDTH-1:0]  addr_gen();
        if (op) begin
            if (WR_ADDR == "incr") begin
                addr = prev_addr + 4; // Increment by 4 to keep word alignment
            end else if (WR_ADDR == "decr") begin
                addr = prev_addr - 4; // Decrement by 4 to keep word alignment
            end else if (WR_ADDR == "rand") begin
                addr = $urandom_range(0, `DEPTH) & ~3; // Random address but word aligned
            end
            end else begin
            if (RD_ADDR == "incr") begin
                addr = prev_addr + 4; // Increment by 4 to keep word alignment
            end else if (RD_ADDR == "decr") begin
                addr = prev_addr - 4; // Decrement by 4 to keep word alignment
            end else if (WR_ADDR == "rand") begin
                addr = $urandom_range(0, `DEPTH) & ~3; // Random address but word aligned
            end
        end

        prev_addr = addr;
        return addr;

    endfunction

    // Method to capture plusargs
    function void capture_plusargs();
        if ($value$plusargs("WORD_KNOB=%d", WORD_KNOB))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("WORD_KNOB set from command line: %0d", WORD_KNOB), UVM_LOW)
        else
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("Default WORD_KNOB value: %0d", WORD_KNOB), UVM_LOW);

        if ($value$plusargs("HALF_WORD_KNOB=%d", HALF_WORD_KNOB))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("HALF_WORD_KNOB set from command line: %0d", HALF_WORD_KNOB), UVM_LOW)
        else
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("Default HALF_WORD_KNOB value: %0d", HALF_WORD_KNOB), UVM_LOW);

        if ($value$plusargs("BYTE_KNOB=%d", BYTE_KNOB))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("BYTE_KNOB set from command line: %0d", BYTE_KNOB), UVM_LOW)
        else
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("Default BYTE_KNOB value: %0d", BYTE_KNOB), UVM_LOW);

        if ($value$plusargs("WR_ADDR=%s", WR_ADDR))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("WR_ADDR set from command line: %s", WR_ADDR), UVM_LOW)
        else
            WR_ADDR = "rand";

        if ($value$plusargs("RD_ADDR=%s", RD_ADDR))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("RD_ADDR set from command line: %s", RD_ADDR), UVM_LOW)
        else
            RD_ADDR = "rand";

        if ($value$plusargs("LOC=%s", LOC))
            `uvm_info("cont_wr_rd_knobs_loc_seq.sv", $sformatf("LOC set from command line: %s", LOC), UVM_LOW)
        else
            LOC = "RandL1";
        
        endfunction

    // Method to handle half word strobe location
    function bit[`BYTE_LANE-1:0] hw_strobe_handle();
       if (LOC=="ALincr") begin
    		   
    		case(temp_strb)
                4'b0011: temp_strb = 4'b1100;  // Move to the next byte lane
                4'b1100: temp_strb = 4'b0011;  // Move to the next byte lane
                default: temp_strb = 4'b0011;  // Default to the first byte lane
    		endcase
    		  
        end else if (LOC=="ALdecr")begin
    			
            case (temp_strb)
                4'b1100: temp_strb = 4'b0011;  // Move to the previous byte lane
                4'b0011: temp_strb = 4'b1100;  // Move to the previous byte lane
                default: temp_strb = 4'b1100;  // Default to the last byte lane
            endcase
    		
        end
          	return temp_strb;
    endfunction

    // Method to handle byte strobe location
    function bit[`BYTE_LANE-1:0] byte_strobe_handle();
       if (LOC=="ALincr") begin
    		   
    		case(temp_strb)
                4'b0001: temp_strb = 4'b0010;  // Move to the next byte lane
                4'b0010: temp_strb = 4'b0100;  // Move to the next byte lane
                4'b0100: temp_strb = 4'b1000;  // Move to the next byte lane
                4'b1000: temp_strb = 4'b0001;  // Wrap around to the first byte lane
                default: temp_strb = 4'b0001;  // Default to the first byte lane
    		endcase
    		  
        end else if (LOC=="ALdecr")begin
    			
            case (temp_strb)
                4'b1000: temp_strb = 4'b0100;  // Move to the previous byte lane
                4'b0100: temp_strb = 4'b0010;  // Move to the previous byte lane
                4'b0010: temp_strb = 4'b0001;  // Move to the previous byte lane
                4'b0001: temp_strb = 4'b1000;  // Wrap around to the last byte lane
                default: temp_strb = 4'b1000;  // Default to the last byte lane
            endcase
    		
        end
    	return temp_strb;
    endfunction
    

    // Constructor
    function new (string name = "cont_wr_rd_knobs_loc_seq");
        super.new (name);
        capture_plusargs();  // calling plusargs
    endfunction
    
    // Body Task
    virtual task body();
         `uvm_info (get_name(), $sformatf("Start  >>>  %s", get_type_name()), UVM_NONE)
            
            //---------------
           // Reset Sequence
           //----------------

            rst_seq = apb_reset_seq::type_id::create("apb_rst");
			rst_seq.start(m_sequencer, this);

            //---------------
            // Write Sequence
            //----------------

            first_addr = $urandom_range(0, `DEPTH) & ~3 ; // Assigning random address from which address will increase or decrease

            prev_addr = first_addr;

            repeat(iter_count) begin
                wr_seq = apb_directed_seq::type_id::create("wr_seq");
                op = 1'b1;
               // wr_seq.op   = op;
               // wr_seq.data = $random;
               // $display("wr_strb = %b | strb = %b", wr_seq.strb, strb);
                this.randomize();
                wr_seq.strb = temp_strb;
                wr_seq.addr = addr_gen();
		      
               //-------------
               // Byte Knob
               //-------------
                if (temp_strb inside {4'b1000, 4'b0100, 4'b0010, 4'b0001}) begin

                    if (LOC == "RandL1") begin 
                         // temp_strb=byte_strobe_handle();
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);

                    end

                    else if (LOC == "RandL2") begin 
                        repeat(2) begin
                        // temp_strb=byte_strobe_handle();
                        this.randomize() with {temp_strb inside {4'b1000, 4'b0100, 4'b0010, 4'b0001};};
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);
                         end

                    end

                    else if (LOC == "RandL3") begin 
                         repeat(3) begin
                        // temp_strb=byte_strobe_handle();
                        this.randomize() with {temp_strb inside {4'b1000, 4'b0100, 4'b0010, 4'b0001};};
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);
                         end

                    end else begin

                         repeat(4) begin
                         temp_strb=byte_strobe_handle();
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);
                         end

                    end
                
                //----------------
                // Half-word Knob
                //----------------
                end else if (temp_strb inside {4'b0011, 4'b1100}) begin
                     if (LOC == "RandL1" | LOC == "RandL2" | LOC == "RandL3" ) begin
                        // temp_strb=hw_strobe_handle();
                        this.randomize() with {temp_strb inside {4'b0011, 4'b1100};};
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);
                     end
                     else if (LOC == "ALincr" | LOC == "ALdecr") begin
                         repeat(2) begin
                         temp_strb=hw_strobe_handle();
                         wr_seq.op   = op;
                         wr_seq.data = $random;
                         wr_seq.strb = temp_strb;
                         wr_seq.start(m_sequencer,this);
                         end
                     end
                
                //----------
                // Word knob
                //----------
                end else if (temp_strb inside {4'b1111}) begin
                    wr_seq.op   = op;
                    wr_seq.data = $random;
                    wr_seq.strb = temp_strb;
                    wr_seq.start(m_sequencer,this);
                end
                //wr_seq.start(m_sequencer, this);
            end

            //---------------
            // Read Sequence
            //---------------

            rd_seq = apb_directed_seq::type_id::create("rd_seq");

            // incr / decr WR_RD_KNOB logic 
            if (RD_ADDR=="incr" && WR_ADDR=="decr") begin
                     prev_addr = prev_addr - 4; // For read incr from same address
            end
            else if (RD_ADDR=="decr" && WR_ADDR=="incr") begin
                    prev_addr = prev_addr + 4; // For read decr from same address
            end
            else  begin
                    prev_addr = first_addr;
            end
                   
            repeat(iter_count) begin
                op = 1'b0;
                rd_seq.op = op;
                rd_seq.strb = 4'b0000;
                rd_seq.addr = addr_gen();
			    rd_seq.start(m_sequencer, this);
            end

	     `uvm_info (get_name(), $sformatf("END  >>>  %s", get_type_name()), UVM_NONE)

    endtask

    // constraints
    constraint weighted_strb_c {
        rand_val dist {
            0 :/ WORD_KNOB,
            1 :/ HALF_WORD_KNOB,
            2 :/ BYTE_KNOB
        };

        if (rand_val == 0) temp_strb inside {4'b1111};
        else if (rand_val == 1) temp_strb inside {4'b0011, 4'b1100};
        else if (rand_val == 2) temp_strb inside {4'b1000, 4'b0100, 4'b0010, 4'b0001};
    }

endclass
