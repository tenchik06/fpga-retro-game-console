`timescale 1ns/1ps

module tb_vga;
    reg clk;
    wire hsync, vsync, display_on;
    wire [9:0] x_pos, y_pos;
    
    vga_controller dut(
        .clk(clk),
        .hsync(hsync),
        .vsync(vsync),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .display_on(display_on)
    );
    
    initial begin
        clk = 0;
        forever #10 clk = ~clk; // 50MHz
    end
    
    initial begin
        $dumpfile("vga_wave.vcd");
        $dumpvars(0, tb_vga);
        #1000000 $finish;
    end
endmodule