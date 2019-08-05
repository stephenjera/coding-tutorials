; Delay subroutine
; Delay in machine cycles = 1+(x(((1+2)+((y(1+1+2))))
;
			SJMP START
;
			ORG 00040H
;
START:		MOV A,#000H		; Reset ACC
			MOV P0,A		; Move ACC to P0
NEXT:		MOV R4,#00AH	; Select 10 delay loops
			CALL DELAY		; Call DELAY routine
			INC A			; Increment ACC
			MOV P0,A
			SJMP NEXT		; Go to NEXT
;
			ORG 000100H
;
;			Delay subroutine
;
DELAY: 		MOV R2,#001H	; Reset R2
D2: 		MOV R3,#003H	; Reset R3
D3:			NOP				; Waste some time 
			NOP				; Waste more time
			DJNZ R3,D3		; Count down R3 then to D3
			DJNZ R2,D2		; Count down R2 then to D2
			DJNZ R4,DELAY	; Count down number set at next
			MOV P0,A		
;
			RET				; Return froms subroutine
;
			END