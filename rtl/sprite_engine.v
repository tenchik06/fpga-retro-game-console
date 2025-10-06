module sprite_engine(
    input wire clk,
    input wire [9:0] x_pos,
    input wire [9:0] y_pos,
    input wire [9:0] sprite_x,    // X позиция спрайта
    input wire [9:0] sprite_y,    // Y позиция спрайта
    output reg pixel_out
);
    
    // Память для спрайта 16x16
    reg [15:0] sprite_memory [0:15];
    
    // Инициализация спрайта (динозаврик)
    initial begin
        sprite_memory[0]  = 16'b0000000001110000;
        sprite_memory[1]  = 16'b0000000011111000;
        sprite_memory[2]  = 16'b0000000011111000;
        sprite_memory[3]  = 16'b0000000011111000;
        sprite_memory[4]  = 16'b0000000011111000;
        sprite_memory[5]  = 16'b0000000011110000;
        sprite_memory[6]  = 16'b0000111111110000;
        sprite_memory[7]  = 16'b0011111111111000;
        sprite_memory[8]  = 16'b0111111111111100;
        sprite_memory[9]  = 16'b1111111111111100;
        sprite_memory[10] = 16'b1111111111111100;
        sprite_memory[11] = 16'b1111111111111000;
        sprite_memory[12] = 16'b0111111111110000;
        sprite_memory[13] = 16'b0001111111100000;
        sprite_memory[14] = 16'b0000111111000000;
        sprite_memory[15] = 16'b0000011110000000;
    end
    
    wire [3:0] sprite_pixel_x = x_pos - sprite_x;
    wire [3:0] sprite_pixel_y = y_pos - sprite_y;
    
    wire in_sprite_area = (x_pos >= sprite_x) && 
                         (x_pos < sprite_x + 16) && 
                         (y_pos >= sprite_y) && 
                         (y_pos < sprite_y + 16);
    
    always @(posedge clk) begin
        if (in_sprite_area) begin
            // Вывод соответствующего бита из спрайта
            pixel_out <= sprite_memory[sprite_pixel_y][15 - sprite_pixel_x];
        end else begin
            pixel_out <= 0;
        end
    end
endmodule