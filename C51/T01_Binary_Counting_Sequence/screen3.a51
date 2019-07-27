; Test program 
;
		SJMP	START
		ORG		00040H
;		
START:	MOV		A,#000H 	; Set accumulator to zero
		MOV		P0,A		; Move accumulator to port 0
NEXT:   INC		A			; Increment accumulator 
		MOV  	P0,A		; Move accumulator to port 0
		SJMP	NEXT		; Jump to instruction at NEXT
;
END