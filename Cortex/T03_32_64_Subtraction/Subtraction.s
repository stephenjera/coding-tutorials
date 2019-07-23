  ; 32 and 64 bit subtraction 
  ; Set up exception address 
  THUMB
  AREA RESET, DATA, READONLY
  EXPORT __Vectors
  EXPORT Reset_Handler
__Vectors
  DCD 0x20001000 ; Top of the stack
  DCD Reset_Handler ; Where the program starts 
	
  AREA Subtract, CODE, READONLY 
Reset_Handler 
  ENTRY ; First instruction 
subtraction_32_bit
  ;MOV32 r0, 2_10000000000000000000000000000110 ; binary 32-bit minuend
  MOV32 r0, 0x80000006 ; Hex 32-bit minuend 
  ;MOV32 r1, 2_00000000000000000000000000000110 ; binary 32-bit subtrahend
  MOV32 r1, 0x00000003 ; Hex 32-bit subtrahend 
  SUB r2,r0,r1 ; Diffenence of two numbers
  
subtraction_64_bit
  MOV32 r3, 0x80000006 ; Hex 32-bit minuend high word
  MOV32 r4, 0x00000006 ; Hex 32-bit minuend low word
  MOV32 r5, 0x10000006 ; Hex 32-bit subtrahend high word
  MOV32 r6, 0x80000006 ; Hex 32-bit subtrahend low word
  SUBS  r7,r3,r5	   ; High word subtraction
  SBC   r8,r4,r6	   ; Low word subtraction 
terminate ; Sit in an endless loop 
  B terminate 
  END ; End of the program 