  ; Program to perform some internal operations
  ; Set up the exception addresses
  THUMB
  AREA RESET, DATA, READONLY ; An "area" is a AREA is a section of data or code that is manipulated by the linker. 
							 ; Reset area sets up initial status of Cortex m3
							 ; Data is used to hold application code
  EXPORT  __Vectors
  EXPORT Reset_Handler
__Vectors 
  DCD 0x20001000     ; top of the stack 
  DCD Reset_Handler  ; reset vector - where the program starts

  ; The code performs an example of 32-bit and 64-bit addition
  AREA Ex1a, CODE, READONLY ; name the block
  ENTRY   ; mark first instruction (entry directive)
Reset_Handler
  MOV r6,#10  ; first argument
  MOV r7,#20  ; second argument
  ADD r8,r6,r7  ; perform 32-bit operation
do_64_bit_add
  MOV r0,#0xffffffff ; first argument, low word (note 0x means hex)
  MOV r1,#0    ; first argument, high word
  MOV r2,#0x1  ; second argument, low word
  MOV r3,#0    ; second argument, high word
  ADDS r4,r0,r2  ; low word operation
  ADC r5,r1,r3   ; high word operation
terminate  ; sit in an endless loop
  B terminate
  END  ; end of the program (end directive)
