from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_axi_dma_stride

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("_memory_memimg_.out", _memory_mem);
  end

  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
  assign memory_awaddr = myaxi_awaddr;
  assign memory_awlen = myaxi_awlen;
  assign memory_awvalid = myaxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    myaxi_awready = _tmp_0;
  end

  assign memory_wdata = myaxi_wdata;
  assign memory_wstrb = myaxi_wstrb;
  assign memory_wlast = myaxi_wlast;
  assign memory_wvalid = myaxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    myaxi_wready = _tmp_1;
  end

  assign memory_araddr = myaxi_araddr;
  assign memory_arlen = myaxi_arlen;
  assign memory_arvalid = myaxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_2;
  end


  always @(*) begin
    myaxi_rdata <= memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_4;
  end

  assign memory_rready = myaxi_rready;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    memory_awready = 0;
    memory_wready = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_fsm = _memory_fsm_init;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_count = 0;
    _d1__memory_fsm = _memory_fsm_init;
    __memory_fsm_cond_100_0_1 = 0;
    __memory_fsm_cond_200_1_1 = 0;
    __memory_fsm_cond_211_2_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end

  localparam _memory_fsm_200 = 200;
  localparam _memory_fsm_201 = 201;
  localparam _memory_fsm_202 = 202;
  localparam _memory_fsm_203 = 203;
  localparam _memory_fsm_204 = 204;
  localparam _memory_fsm_205 = 205;
  localparam _memory_fsm_206 = 206;
  localparam _memory_fsm_207 = 207;
  localparam _memory_fsm_208 = 208;
  localparam _memory_fsm_209 = 209;
  localparam _memory_fsm_210 = 210;
  localparam _memory_fsm_211 = 211;
  localparam _memory_fsm_100 = 100;
  localparam _memory_fsm_101 = 101;
  localparam _memory_fsm_102 = 102;
  localparam _memory_fsm_103 = 103;
  localparam _memory_fsm_104 = 104;
  localparam _memory_fsm_105 = 105;
  localparam _memory_fsm_106 = 106;
  localparam _memory_fsm_107 = 107;
  localparam _memory_fsm_108 = 108;
  localparam _memory_fsm_109 = 109;
  localparam _memory_fsm_110 = 110;
  localparam _memory_fsm_111 = 111;
  localparam _memory_fsm_112 = 112;

  always @(posedge CLK) begin
    if(RST) begin
      _memory_fsm <= _memory_fsm_init;
      _d1__memory_fsm <= _memory_fsm_init;
      memory_awready <= 0;
      _write_addr <= 0;
      _write_count <= 0;
      __memory_fsm_cond_100_0_1 <= 0;
      memory_wready <= 0;
      memory_arready <= 0;
      _read_addr <= 0;
      _read_count <= 0;
      __memory_fsm_cond_200_1_1 <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      _sleep_count <= 0;
    end else begin
      _sleep_count <= _sleep_count + 1;
      if(_sleep_count == 3) begin
        _sleep_count <= 0;
      end 
      _d1__memory_fsm <= _memory_fsm;
      case(_d1__memory_fsm)
        _memory_fsm_100: begin
          if(__memory_fsm_cond_100_0_1) begin
            memory_awready <= 0;
          end 
        end
        _memory_fsm_200: begin
          if(__memory_fsm_cond_200_1_1) begin
            memory_arready <= 0;
          end 
        end
        _memory_fsm_211: begin
          if(__memory_fsm_cond_211_2_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_fsm)
        _memory_fsm_init: begin
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_100;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_200;
          end 
        end
        _memory_fsm_100: begin
          if(memory_awvalid) begin
            memory_awready <= 1;
            _write_addr <= memory_awaddr;
            _write_count <= memory_awlen + 1;
          end 
          __memory_fsm_cond_100_0_1 <= 1;
          if(!memory_awvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_101;
          end 
        end
        _memory_fsm_101: begin
          _memory_fsm <= _memory_fsm_102;
        end
        _memory_fsm_102: begin
          _memory_fsm <= _memory_fsm_103;
        end
        _memory_fsm_103: begin
          _memory_fsm <= _memory_fsm_104;
        end
        _memory_fsm_104: begin
          _memory_fsm <= _memory_fsm_105;
        end
        _memory_fsm_105: begin
          _memory_fsm <= _memory_fsm_106;
        end
        _memory_fsm_106: begin
          _memory_fsm <= _memory_fsm_107;
        end
        _memory_fsm_107: begin
          _memory_fsm <= _memory_fsm_108;
        end
        _memory_fsm_108: begin
          _memory_fsm <= _memory_fsm_109;
        end
        _memory_fsm_109: begin
          _memory_fsm <= _memory_fsm_110;
        end
        _memory_fsm_110: begin
          _memory_fsm <= _memory_fsm_111;
        end
        _memory_fsm_111: begin
          memory_wready <= 1;
          _memory_fsm <= _memory_fsm_112;
        end
        _memory_fsm_112: begin
          if(memory_wvalid && memory_wstrb[0]) begin
            _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
          end 
          if(memory_wvalid && memory_wstrb[1]) begin
            _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
          end 
          if(memory_wvalid && memory_wstrb[2]) begin
            _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
          end 
          if(memory_wvalid && memory_wstrb[3]) begin
            _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_count == 3) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
        _memory_fsm_200: begin
          if(memory_arvalid) begin
            memory_arready <= 1;
            _read_addr <= memory_araddr;
            _read_count <= memory_arlen + 1;
          end 
          __memory_fsm_cond_200_1_1 <= 1;
          if(!memory_arvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_201;
          end 
        end
        _memory_fsm_201: begin
          _memory_fsm <= _memory_fsm_202;
        end
        _memory_fsm_202: begin
          _memory_fsm <= _memory_fsm_203;
        end
        _memory_fsm_203: begin
          _memory_fsm <= _memory_fsm_204;
        end
        _memory_fsm_204: begin
          _memory_fsm <= _memory_fsm_205;
        end
        _memory_fsm_205: begin
          _memory_fsm <= _memory_fsm_206;
        end
        _memory_fsm_206: begin
          _memory_fsm <= _memory_fsm_207;
        end
        _memory_fsm_207: begin
          _memory_fsm <= _memory_fsm_208;
        end
        _memory_fsm_208: begin
          _memory_fsm <= _memory_fsm_209;
        end
        _memory_fsm_209: begin
          _memory_fsm <= _memory_fsm_210;
        end
        _memory_fsm_210: begin
          _memory_fsm <= _memory_fsm_211;
        end
        _memory_fsm_211: begin
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[7:0] <= _memory_mem[_read_addr + 0];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[15:8] <= _memory_mem[_read_addr + 1];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[23:16] <= _memory_mem[_read_addr + 2];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[31:24] <= _memory_mem[_read_addr + 3];
          end 
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 4;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_count < 3) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_fsm_cond_211_2_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_size;
  reg [32-1:0] _myaxi_read_local_stride;
  reg _myaxi_read_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_size;
  reg [32-1:0] _myaxi_write_local_stride;
  reg _myaxi_write_idle;
  wire _myaxi_write_data_done;
  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg _tmp_0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_i_5;
  reg signed [32-1:0] _th_blink_wdata_6;
  reg _myram_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_7;
  reg signed [32-1:0] _th_blink_gaddr_8;
  reg axim_flag_1;
  reg [32-1:0] _d1_th_blink;
  reg _th_blink_cond_14_0_1;
  reg _myaxi_myram_0_write_start;
  reg [8-1:0] _myaxi_myram_0_write_op_sel;
  reg [32-1:0] _myaxi_myram_0_write_local_addr;
  reg [32-1:0] _myaxi_myram_0_write_global_addr;
  reg [33-1:0] _myaxi_myram_0_write_size;
  reg [32-1:0] _myaxi_myram_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
  reg _tmp_2;
  reg _tmp_3;
  wire _tmp_4;
  wire _tmp_5;
  assign _tmp_5 = 1;
  localparam _tmp_6 = 1;
  wire [_tmp_6-1:0] _tmp_7;
  assign _tmp_7 = (_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3);
  reg [_tmp_6-1:0] __tmp_7_1;
  wire signed [32-1:0] _tmp_8;
  reg signed [32-1:0] __tmp_8_1;
  assign _tmp_8 = (__tmp_7_1)? myram_0_rdata : __tmp_8_1;
  reg _tmp_9;
  reg _tmp_10;
  reg _tmp_11;
  reg _tmp_12;
  reg [34-1:0] _tmp_13;
  reg [9-1:0] _tmp_14;
  reg _myaxi_cond_0_1;
  reg _tmp_15;
  wire [32-1:0] __variable_data_16;
  wire __variable_valid_16;
  wire __variable_ready_16;
  assign __variable_ready_16 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_14 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  assign _myaxi_write_data_done = (_tmp_15 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_17;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg signed [32-1:0] _th_blink_lstride_9;
  reg axim_flag_18;
  reg _th_blink_cond_19_1_1;
  reg _myram_cond_1_1;
  reg axim_flag_19;
  reg _th_blink_cond_31_2_1;
  reg axim_flag_20;
  reg _th_blink_cond_36_3_1;
  reg axim_flag_21;
  reg _th_blink_cond_43_4_1;
  reg _myaxi_myram_0_read_start;
  reg [8-1:0] _myaxi_myram_0_read_op_sel;
  reg [32-1:0] _myaxi_myram_0_read_local_addr;
  reg [32-1:0] _myaxi_myram_0_read_global_addr;
  reg [33-1:0] _myaxi_myram_0_read_size;
  reg [32-1:0] _myaxi_myram_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [32-1:0] _wdata_22;
  reg _wvalid_23;
  reg [34-1:0] _tmp_24;
  reg _tmp_25;
  wire [32-1:0] __variable_data_26;
  wire __variable_valid_26;
  wire __variable_ready_26;
  assign __variable_ready_26 = (_tmp_24 > 0) && !_tmp_25;
  reg _myram_cond_2_1;
  reg [9-1:0] _tmp_27;
  reg _myaxi_cond_2_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_28;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg axim_flag_29;
  reg _th_blink_cond_48_5_1;
  reg _tmp_30;
  reg _myram_cond_3_1;
  reg _myram_cond_4_1;
  reg _myram_cond_4_2;
  reg signed [32-1:0] _tmp_31;
  reg signed [32-1:0] _th_blink_rdata_10;
  reg axim_flag_32;
  reg _th_blink_cond_63_6_1;
  reg axim_flag_33;
  reg _th_blink_cond_68_7_1;
  reg _tmp_34;
  reg _myram_cond_5_1;
  reg _myram_cond_6_1;
  reg _myram_cond_6_2;
  reg signed [32-1:0] _tmp_35;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      _myaxi_myram_0_write_op_sel <= 0;
      _myaxi_myram_0_write_local_addr <= 0;
      _myaxi_myram_0_write_global_addr <= 0;
      _myaxi_myram_0_write_size <= 0;
      _myaxi_myram_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_14 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_15 <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_myram_0_read_start <= 0;
      _myaxi_myram_0_read_op_sel <= 0;
      _myaxi_myram_0_read_local_addr <= 0;
      _myaxi_myram_0_read_global_addr <= 0;
      _myaxi_myram_0_read_size <= 0;
      _myaxi_myram_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_27 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_15 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_arvalid <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      if(axim_flag_1) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_7;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_8;
        _myaxi_myram_0_write_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_write_local_stride <= 2;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_myram_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_myram_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_myram_0_write_global_addr;
        _myaxi_write_size <= _myaxi_myram_0_write_size;
        _myaxi_write_local_stride <= _myaxi_myram_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_14 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_14 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_14 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_16 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_14 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_14 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_14 > 0))) begin
        myaxi_wdata <= __variable_data_16;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_14 <= _tmp_14 - 1;
      end 
      if(__variable_valid_16 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_14 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_14 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_14 > 0)) && (_tmp_14 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_15 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_15 <= _tmp_15;
      end 
      if(axim_flag_17) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_18) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_7 + 1;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
        _myaxi_myram_0_write_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_write_local_stride <= _th_blink_lstride_9;
      end 
      if(axim_flag_19) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_7;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_8;
        _myaxi_myram_0_write_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_write_local_stride <= 2;
      end 
      if(axim_flag_20) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_7 + 1;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
        _myaxi_myram_0_write_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_write_local_stride <= _th_blink_lstride_9;
      end 
      _myaxi_myram_0_read_start <= 0;
      if(axim_flag_21) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_7;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_8;
        _myaxi_myram_0_read_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_read_local_stride <= 2;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_myram_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_myram_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_myram_0_read_global_addr;
        _myaxi_read_size <= _myaxi_myram_0_read_size;
        _myaxi_read_local_stride <= _myaxi_myram_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_27 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_27 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_27 > 0)) begin
        _tmp_27 <= _tmp_27 - 1;
      end 
      if(axim_flag_28) begin
        _myaxi_read_idle <= 1;
      end 
      if(axim_flag_29) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_7 + 1;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
        _myaxi_myram_0_read_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_read_local_stride <= _th_blink_lstride_9;
      end 
      if(axim_flag_32) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_7;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_8;
        _myaxi_myram_0_read_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_read_local_stride <= 2;
      end 
      if(axim_flag_33) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_7 + 1;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
        _myaxi_myram_0_read_size <= _th_blink_size_3 >>> 1;
        _myaxi_myram_0_read_local_stride <= _th_blink_lstride_9;
      end 
    end
  end

  assign __variable_data_26 = _wdata_22;
  assign __variable_valid_26 = _wvalid_23;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      __tmp_7_1 <= 0;
      __tmp_8_1 <= 0;
      _tmp_12 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_9 <= 0;
      _tmp_13 <= 0;
      _myram_cond_1_1 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_3_1 <= 0;
      _tmp_30 <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_4_2 <= 0;
      _myram_cond_5_1 <= 0;
      _tmp_34 <= 0;
      _myram_cond_6_1 <= 0;
      _myram_cond_6_2 <= 0;
    end else begin
      if(_myram_cond_4_2) begin
        _tmp_30 <= 0;
      end 
      if(_myram_cond_6_2) begin
        _tmp_34 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_2_1) begin
        myram_0_wenable <= 0;
        _tmp_25 <= 0;
      end 
      if(_myram_cond_3_1) begin
        _tmp_30 <= 1;
      end 
      _myram_cond_4_2 <= _myram_cond_4_1;
      if(_myram_cond_5_1) begin
        _tmp_34 <= 1;
      end 
      _myram_cond_6_2 <= _myram_cond_6_1;
      if(th_blink == 10) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 10;
      __tmp_7_1 <= _tmp_7;
      __tmp_8_1 <= _tmp_8;
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_10) begin
        _tmp_12 <= 0;
        _tmp_2 <= 0;
        _tmp_3 <= 0;
        _tmp_10 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_9) begin
        _tmp_2 <= 1;
        _tmp_3 <= 1;
        _tmp_12 <= _tmp_11;
        _tmp_11 <= 0;
        _tmp_9 <= 0;
        _tmp_10 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_13 == 0) && !_tmp_11 && !_tmp_12) begin
        myram_0_addr <= _myaxi_write_local_addr;
        _tmp_13 <= _myaxi_write_size - 1;
        _tmp_9 <= 1;
        _tmp_11 <= _myaxi_write_size == 1;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 > 0)) begin
        myram_0_addr <= myram_0_addr + _myaxi_write_local_stride;
        _tmp_13 <= _tmp_13 - 1;
        _tmp_9 <= 1;
        _tmp_11 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 == 1)) begin
        _tmp_11 <= 1;
      end 
      if(th_blink == 27) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_1_1 <= th_blink == 27;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_24 == 0)) begin
        myram_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_24 <= _myaxi_read_size;
      end 
      if(__variable_valid_26 && ((_tmp_24 > 0) && !_tmp_25) && (_tmp_24 > 0)) begin
        myram_0_addr <= myram_0_addr + _myaxi_read_local_stride;
        myram_0_wdata <= __variable_data_26;
        myram_0_wenable <= 1;
        _tmp_24 <= _tmp_24 - 1;
      end 
      if(__variable_valid_26 && ((_tmp_24 > 0) && !_tmp_25) && (_tmp_24 == 1)) begin
        _tmp_25 <= 1;
      end 
      _myram_cond_2_1 <= 1;
      if(th_blink == 55) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_3_1 <= th_blink == 55;
      _myram_cond_4_1 <= th_blink == 55;
      if(th_blink == 75) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_5_1 <= th_blink == 75;
      _myram_cond_6_1 <= th_blink == 75;
    end
  end

  assign __variable_data_16 = _tmp_8;
  assign __variable_valid_16 = _tmp_2;
  assign _tmp_4 = 1 && __variable_ready_16;
  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;
  localparam th_blink_28 = 28;
  localparam th_blink_29 = 29;
  localparam th_blink_30 = 30;
  localparam th_blink_31 = 31;
  localparam th_blink_32 = 32;
  localparam th_blink_33 = 33;
  localparam th_blink_34 = 34;
  localparam th_blink_35 = 35;
  localparam th_blink_36 = 36;
  localparam th_blink_37 = 37;
  localparam th_blink_38 = 38;
  localparam th_blink_39 = 39;
  localparam th_blink_40 = 40;
  localparam th_blink_41 = 41;
  localparam th_blink_42 = 42;
  localparam th_blink_43 = 43;
  localparam th_blink_44 = 44;
  localparam th_blink_45 = 45;
  localparam th_blink_46 = 46;
  localparam th_blink_47 = 47;
  localparam th_blink_48 = 48;
  localparam th_blink_49 = 49;
  localparam th_blink_50 = 50;
  localparam th_blink_51 = 51;
  localparam th_blink_52 = 52;
  localparam th_blink_53 = 53;
  localparam th_blink_54 = 54;
  localparam th_blink_55 = 55;
  localparam th_blink_56 = 56;
  localparam th_blink_57 = 57;
  localparam th_blink_58 = 58;
  localparam th_blink_59 = 59;
  localparam th_blink_60 = 60;
  localparam th_blink_61 = 61;
  localparam th_blink_62 = 62;
  localparam th_blink_63 = 63;
  localparam th_blink_64 = 64;
  localparam th_blink_65 = 65;
  localparam th_blink_66 = 66;
  localparam th_blink_67 = 67;
  localparam th_blink_68 = 68;
  localparam th_blink_69 = 69;
  localparam th_blink_70 = 70;
  localparam th_blink_71 = 71;
  localparam th_blink_72 = 72;
  localparam th_blink_73 = 73;
  localparam th_blink_74 = 74;
  localparam th_blink_75 = 75;
  localparam th_blink_76 = 76;
  localparam th_blink_77 = 77;
  localparam th_blink_78 = 78;
  localparam th_blink_79 = 79;
  localparam th_blink_80 = 80;
  localparam th_blink_81 = 81;
  localparam th_blink_82 = 82;
  localparam th_blink_83 = 83;
  localparam th_blink_84 = 84;
  localparam th_blink_85 = 85;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _d1_th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_i_5 <= 0;
      _th_blink_wdata_6 <= 0;
      _th_blink_laddr_7 <= 0;
      _th_blink_gaddr_8 <= 0;
      axim_flag_1 <= 0;
      _th_blink_cond_14_0_1 <= 0;
      _th_blink_lstride_9 <= 0;
      axim_flag_18 <= 0;
      _th_blink_cond_19_1_1 <= 0;
      axim_flag_19 <= 0;
      _th_blink_cond_31_2_1 <= 0;
      axim_flag_20 <= 0;
      _th_blink_cond_36_3_1 <= 0;
      axim_flag_21 <= 0;
      _th_blink_cond_43_4_1 <= 0;
      axim_flag_29 <= 0;
      _th_blink_cond_48_5_1 <= 0;
      _tmp_31 <= 0;
      _th_blink_rdata_10 <= 0;
      axim_flag_32 <= 0;
      _th_blink_cond_63_6_1 <= 0;
      axim_flag_33 <= 0;
      _th_blink_cond_68_7_1 <= 0;
      _tmp_35 <= 0;
    end else begin
      _d1_th_blink <= th_blink;
      case(_d1_th_blink)
        th_blink_14: begin
          if(_th_blink_cond_14_0_1) begin
            axim_flag_1 <= 0;
          end 
        end
        th_blink_19: begin
          if(_th_blink_cond_19_1_1) begin
            axim_flag_18 <= 0;
          end 
        end
        th_blink_31: begin
          if(_th_blink_cond_31_2_1) begin
            axim_flag_19 <= 0;
          end 
        end
        th_blink_36: begin
          if(_th_blink_cond_36_3_1) begin
            axim_flag_20 <= 0;
          end 
        end
        th_blink_43: begin
          if(_th_blink_cond_43_4_1) begin
            axim_flag_21 <= 0;
          end 
        end
        th_blink_48: begin
          if(_th_blink_cond_48_5_1) begin
            axim_flag_29 <= 0;
          end 
        end
        th_blink_63: begin
          if(_th_blink_cond_63_6_1) begin
            axim_flag_32 <= 0;
          end 
        end
        th_blink_68: begin
          if(_th_blink_cond_68_7_1) begin
            axim_flag_33 <= 0;
          end 
        end
      endcase
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 16;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _tmp_0 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_1 < 4) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_83;
          end
        end
        th_blink_4: begin
          $display("# iter %d start", _th_blink_i_1);
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_offset_2 <= ((_th_blink_i_1 << 10) << 4) + 4092;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_size_3 <= _th_blink_size_0;
          _th_blink_offset_4 <= _th_blink_offset_2;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_12;
          end
        end
        th_blink_9: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 100;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_12: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          axim_flag_1 <= 1;
          _th_blink_cond_14_0_1 <= 1;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_18;
          end 
        end
        th_blink_18: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          axim_flag_18 <= 1;
          _th_blink_cond_19_1_1 <= 1;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_23;
          end 
        end
        th_blink_23: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_26;
          end else begin
            th_blink <= th_blink_29;
          end
        end
        th_blink_26: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 1000;
          th_blink <= th_blink_27;
        end
        th_blink_27: begin
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_25;
        end
        th_blink_29: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          axim_flag_19 <= 1;
          _th_blink_cond_31_2_1 <= 1;
          th_blink <= th_blink_32;
        end
        th_blink_32: begin
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_35;
          end 
        end
        th_blink_35: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_36;
        end
        th_blink_36: begin
          axim_flag_20 <= 1;
          _th_blink_cond_36_3_1 <= 1;
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_40;
          end 
        end
        th_blink_40: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_42;
        end
        th_blink_42: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          axim_flag_21 <= 1;
          _th_blink_cond_43_4_1 <= 1;
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_47;
          end 
        end
        th_blink_47: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_48;
        end
        th_blink_48: begin
          axim_flag_29 <= 1;
          _th_blink_cond_48_5_1 <= 1;
          th_blink <= th_blink_49;
        end
        th_blink_49: begin
          th_blink <= th_blink_50;
        end
        th_blink_50: begin
          th_blink <= th_blink_51;
        end
        th_blink_51: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_52;
          end 
        end
        th_blink_52: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_53;
        end
        th_blink_53: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_55;
          end else begin
            th_blink <= th_blink_61;
          end
        end
        th_blink_55: begin
          if(_tmp_30) begin
            _tmp_31 <= myram_0_rdata;
          end 
          if(_tmp_30) begin
            th_blink <= th_blink_56;
          end 
        end
        th_blink_56: begin
          _th_blink_rdata_10 <= _tmp_31;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          if(_th_blink_rdata_10 !== _th_blink_i_5 + 100) begin
            th_blink <= th_blink_58;
          end else begin
            th_blink <= th_blink_60;
          end
        end
        th_blink_58: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_10);
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_54;
        end
        th_blink_61: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_63;
        end
        th_blink_63: begin
          axim_flag_32 <= 1;
          _th_blink_cond_63_6_1 <= 1;
          th_blink <= th_blink_64;
        end
        th_blink_64: begin
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_67;
          end 
        end
        th_blink_67: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          axim_flag_33 <= 1;
          _th_blink_cond_68_7_1 <= 1;
          th_blink <= th_blink_69;
        end
        th_blink_69: begin
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          th_blink <= th_blink_71;
        end
        th_blink_71: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_72;
          end 
        end
        th_blink_72: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_73;
        end
        th_blink_73: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_74;
        end
        th_blink_74: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_75;
          end else begin
            th_blink <= th_blink_81;
          end
        end
        th_blink_75: begin
          if(_tmp_34) begin
            _tmp_35 <= myram_0_rdata;
          end 
          if(_tmp_34) begin
            th_blink <= th_blink_76;
          end 
        end
        th_blink_76: begin
          _th_blink_rdata_10 <= _tmp_35;
          th_blink <= th_blink_77;
        end
        th_blink_77: begin
          if(_th_blink_rdata_10 !== _th_blink_i_5 + 1000) begin
            th_blink <= th_blink_78;
          end else begin
            th_blink <= th_blink_80;
          end
        end
        th_blink_78: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_10);
          th_blink <= th_blink_79;
        end
        th_blink_79: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_80;
        end
        th_blink_80: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_74;
        end
        th_blink_81: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_82;
        end
        th_blink_82: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_83: begin
          if(_tmp_0) begin
            th_blink <= th_blink_84;
          end else begin
            th_blink <= th_blink_85;
          end
        end
        th_blink_84: begin
          $display("ALL OK");
          th_blink <= th_blink_85;
        end
      endcase
    end
  end

  localparam _myaxi_write_fsm_1 = 1;
  localparam _myaxi_write_fsm_2 = 2;
  localparam _myaxi_write_fsm_3 = 3;
  localparam _myaxi_write_fsm_4 = 4;
  localparam _myaxi_write_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_fsm <= _myaxi_write_fsm_init;
      _d1__myaxi_write_fsm <= _myaxi_write_fsm_init;
      _myaxi_write_cur_global_addr <= 0;
      _myaxi_write_rest_size <= 0;
      _myaxi_write_cur_size <= 0;
      axim_flag_17 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_17 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_fsm)
        _myaxi_write_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_cur_global_addr <= (_myaxi_write_global_addr >> 2) << 2;
            _myaxi_write_rest_size <= _myaxi_write_size;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
        end
        _myaxi_write_fsm_1: begin
          if((_myaxi_write_rest_size <= 256) && ((_myaxi_write_cur_global_addr & 4095) + (_myaxi_write_rest_size << 2) >= 4096)) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_write_rest_size <= 256) begin
            _myaxi_write_cur_size <= _myaxi_write_rest_size;
            _myaxi_write_rest_size <= 0;
          end else if((_myaxi_write_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_write_cur_size <= 256;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - 256;
          end
          _myaxi_write_fsm <= _myaxi_write_fsm_2;
        end
        _myaxi_write_fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_3;
          end 
        end
        _myaxi_write_fsm_3: begin
          if(_myaxi_write_data_done) begin
            _myaxi_write_cur_global_addr <= _myaxi_write_cur_global_addr + (_myaxi_write_cur_size << 2);
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size > 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size == 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_4;
          end 
        end
        _myaxi_write_fsm_4: begin
          axim_flag_17 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
        end
      endcase
    end
  end

  localparam _myaxi_read_fsm_1 = 1;
  localparam _myaxi_read_fsm_2 = 2;
  localparam _myaxi_read_fsm_3 = 3;
  localparam _myaxi_read_fsm_4 = 4;
  localparam _myaxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_fsm <= _myaxi_read_fsm_init;
      _d1__myaxi_read_fsm <= _myaxi_read_fsm_init;
      _myaxi_read_cur_global_addr <= 0;
      _myaxi_read_rest_size <= 0;
      _myaxi_read_cur_size <= 0;
      __myaxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_23 <= 0;
      _wdata_22 <= 0;
      axim_flag_28 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_23 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_28 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_fsm)
        _myaxi_read_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_cur_global_addr <= (_myaxi_read_global_addr >> 2) << 2;
            _myaxi_read_rest_size <= _myaxi_read_size;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
        end
        _myaxi_read_fsm_1: begin
          if((_myaxi_read_rest_size <= 256) && ((_myaxi_read_cur_global_addr & 4095) + (_myaxi_read_rest_size << 2) >= 4096)) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_read_rest_size <= 256) begin
            _myaxi_read_cur_size <= _myaxi_read_rest_size;
            _myaxi_read_rest_size <= 0;
          end else if((_myaxi_read_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_read_cur_size <= 256;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - 256;
          end
          _myaxi_read_fsm <= _myaxi_read_fsm_2;
        end
        _myaxi_read_fsm_2: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_3;
          end 
        end
        _myaxi_read_fsm_3: begin
          __myaxi_read_fsm_cond_3_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1)) begin
            _wdata_22 <= myaxi_rdata;
            _wvalid_23 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_28 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_axi_dma_stride.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
