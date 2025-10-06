`timescale 1ns/1ps

module tb_sprite;
    reg clk;
    reg [9:0] x_pos, y_pos;
    wire sprite_pixel;
    
    sprite_engine dut(
        .clk(clk),
        .x_pos(x_pos),
        .y_pos(y_pos),
        .sprite_x(100),
        .sprite_y(150),
        .pixel_out(sprite_pixel)
    );
    
    initial begin
        clk = 0;
        forever #10 clk = ~clk;
    end
    
    initial begin
        $dumpfile("sprite_wave.vcd");
        $dumpvars(0, tb_sprite);
        
        // Тестирование в области спрайта
        x_pos = 100;
        y_pos = 150;
        #20;
        
        // Сканирование по спрайту
        for (y_pos = 150; y_pos < 166; y_pos = y_pos + 1) begin
            for (x_pos = 100; x_pos < 116; x_pos = x_pos + 1) begin
                #20;
            end
        end
        
        #100 $finish;
    end
endmodule