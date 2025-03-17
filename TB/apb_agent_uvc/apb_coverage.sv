class apb_coverage extends uvm_subscriber #(apb_seq_item);
  `uvm_component_utils(apb_coverage)

  // Transaction data handle
  apb_seq_item item;

  real cov_val;

  // Covergroup declaration
  covergroup apb_cg;
    // Coverpoint for reset
    STROBE: coverpoint item.PSTRB_i {
      bins reset_low  = {4'b0000};
      bins reset_mid1 = {4'b0100};
      bins reset_mid2 = {4'b0010};
      bins reset_mid3 = {4'b0001};
      bins reset_mid4 = {4'b0011};
      bins reset_mid5 = {4'b1100};
      bins reset_high = {4'b1111};
    }

    // Coverpoint for address
    PADDR: coverpoint item.PADDR_i {
      bins addr_low  = {[0:(`ADDR_WIDTH/2 - 1)]};
      bins addr_high = {[( `ADDR_WIDTH/2):(`ADDR_WIDTH-1)]};
    }

    // Coverpoint for write data (uncommented and fixed)
    PWDATA: coverpoint item.PWDATA_i {
      bins data_low  = {8'h00};
      bins data_high = {8'hFF};
    }

    // Coverpoint for read data
    PRDATA: coverpoint item.PRDATA_o {
      bins data_low  = {[0:`DATA_WIDTH/2 - 1]};
      bins data_high = {[`DATA_WIDTH/2:`DATA_WIDTH-1]};
    }

    // Control signals
    PWRITE: coverpoint item.PWRITE_i {
      bins pwrite = {1'b1};
      bins pread  = {1'b0};
    }

    PSEL: coverpoint item.PSEL_i {
      bins psel_high = {1'b1};
      bins psel_low  = {1'b0};
    }

    // Cross-coverage for write transactions
    CROSS_WRITE: cross PADDR, PWDATA, PSEL, PWRITE {
      ignore_bins ig1 = binsof(PSEL.psel_low);
      ignore_bins ig2 = binsof(PWRITE.pread);
    }

    // Cross-coverage for read transactions
    CROSS_READ: cross PADDR, PRDATA, PSEL, PWRITE {
      ignore_bins ig3 = binsof(PWRITE.pwrite);
      ignore_bins ig4 = binsof(PSEL.psel_low);
    }
  endgroup

  // Constructor
  function new(string name, uvm_component parent);
    super.new(name, parent);
    apb_cg = new();
  endfunction

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    `uvm_info(get_name(), $sformatf("Coverage Build Phase"), UVM_NONE)
  endfunction

  // Write function to receive data from monitor
  function void write(apb_seq_item t);
    $cast(item, t);
    `uvm_info(get_name(), $sformatf("Received from Monitor: %0d", t.PSTRB_i), UVM_NONE)
    this.item = t;
    apb_cg.sample();
  endfunction

  virtual function void extract_phase(uvm_phase phase);
    super.extract_phase(phase);
    cov_val = apb_cg.get_coverage();
  endfunction : extract_phase

  virtual function void report_phase(uvm_phase phase);
    super.report_phase(phase);
    `uvm_info(get_name(), $sformatf("Sampled coverage = %0f", cov_val), UVM_NONE)
  endfunction : report_phase

endclass