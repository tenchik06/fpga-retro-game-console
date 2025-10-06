module text_renderer(
    input wire clk,
    input wire [9:0] x,
    input wire [9:0] y,
    output reg pixel_out
);
    // Простой шрифт 8x8
    reg [7:0] font [0:255];
    reg [7:0] text_buffer [0:79]; // 80 символов
    
    initial begin
        // Загрузка шрифта (упрощенная версия)
        $readmemh("fonts/pixel_font.hex", font);
        // Инициализация текстового буфера
        text_buffer[0] = "H"; text_buffer[1] = "e"; text_buffer[2] = "l"; 
        text_buffer[3] = "l"; text_buffer[4] = "o"; text_buffer[5] = " ";
        text_buffer[6] = "R"; text_buffer[7] = "e"; text_buffer[8] = "t"; 
        text_buffer[9] = "r"; text_buffer[10] = "o"; text_buffer[11] = "!";
    end
    
    wire [6:0] char_x = x[9:3]; // x/8
    wire [6:0] char_y = y[9:3]; // y/8
    wire [2:0] pixel_x = x[2:0];
    wire [2:0] pixel_y = y[2:0];
    
    wire [6:0] char_index = char_y * 10 + char_x;
    wire [7:0] current_char = (char_index < 80) ? text_buffer[char_index] : 0;
    wire [7:0] font_line = font[{current_char, pixel_y}];
    
    always @(posedge clk) begin
        pixel_out = (char_x < 10 && char_y < 8) ? font_line[7 - pixel_x] : 0;
    end
endmodule