; Compile with command and run: nasm -felf64 project.asm && gcc -no-pie project.o && ./a.out
        global   main           ; for gcc standard linking
	extern printf

%macro  mac_a 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt2       
        mov     rsi, .str       

        mov     rdx, [a]        
        mov     rcx, [m]        
	mov     r8, [c]         
        mov     rax, 0          
        call    printf          
%endmacro

%macro  mac_x 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt3       
        mov     rsi, .str      

        mov     rdx, [x]        
        mov     rcx, [n]        
	mov     r8, [y]         
        mov     rax, 0          
        call    printf          
%endmacro

%macro  mac_i 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt4       
        mov     rsi, .str     

        mov     rdx, [i]        
        mov     rcx, [o]        
	mov     r8, [j]         
        mov     rax, 0          
        call    printf          
%endmacro

%macro  prt_a 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt5       
        mov     rsi, .str       
        mov     rdx, [a]        
	mov     rax, 0          
        call    printf          
%endmacro
%macro  prt_x 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt5       
        mov     rsi, .str       
        mov     rdx, [x]        
	mov     rax, 0          
        call    printf          
%endmacro

%macro  prt_i 1                
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt5       
        mov     rsi, .str       
        mov     rdx, [i]        
	mov     rax, 0          
        call    printf          
%endmacro

%macro  prt_c 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt5      
        mov     rsi, .str       
        mov     rdx, [c]       
	mov     rax, 0          
        call    printf          
%endmacro


%macro  prt_menu 1                 
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt6       
        mov     rsi, .str       
	mov     rax, 0          
        call    printf          
%endmacro

%macro  prt_cont 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt8       
        mov     rsi, .str       
	mov     rax, 0          
        call    printf          
%endmacro

%macro  prt_s 1                  
        section .data
.str    db      %1,0            
        section .text
        mov     rdi, fmt7       
        mov     rsi, .str       
	mov     rax, 0          
        call    printf          
%endmacro


section .data           ; preset constants, writable
	text	 db 	"It's not an integer", 10
        len 	equ $-text
	msg:	db	'Words Words m =', ' %ld', 10, 0
	m:	dq	69		
	a:      dq      5               
	b:      dq      5               

	n:	dq	69		
	x:      dq      5               
	y:      dq      5               

	o:	dq	69		
	i:      dq      5               
	j:      dq      5               
	
	str1 	db 	'fact',10
	str1len	equ 	$-str1
	str2 	db 	'fact',10

	str3 	db 	'comb',10
	
	str4 	db 	'perm',10

	str5 	db 	'yes',10
	str5len	equ 	$-str5
	

fmt2:   db "%s%ld n=%ld",10,0       ; format string for printf

fmt3:   db "%s%ld r=%ld",10,0       ; format string for printf

fmt4:   db "%s%ld (n-r)=%ld",10,0       ; format string for printf

fmt5:   db "%s =%ld ", 10 ,0       ; format string for printf

fmt6:   db "Select one of the following by typing in your choice:", 10, 10, "Factorial.    Enter: fact", 10, "Combinations. Enter: comb", 10, "Permutations. Enter: perm", 10, "Else, Enter any key to exit", 10, 0       ; format string for print

fmt7:   db "%s", 10, 0       ; format string for print

fmt8:   db "Would you like to continue?", 10, "To continue. Enter: yes", 10, "Else, enter any key to exit", 10, 0       ; format string for print

section .bss            ; uninitialized space
	ascii resb 16           ; holds user input
        intMemory resb 100      ; will hold the endline feed 
        intAddress resb 8       ; hold offset address from the intMemory
	
	
num 	resb 	5
c:      resq    1               ; reserve a 64-bit word

        section .text           ; instructions, code segment

main:                           
        push rbp
        
	prt_menu"null" 
	mov rax,0 
        mov rdi,0
        mov rsi,str1
        mov rdx,8
        syscall


        lea esi, [str1]
        lea edi, [str2]
        mov ecx, str1len  ; selects the length of the first string as maximum for comparison
        rep cmpsb         ; comparison of ECX number of bytes
        mov eax, 4        ; does not modify flags 
        mov ebx, 1        ; does not modify flags 
        jne not_fact       ; checks ZERO flag
	jmp ifFact

not_fact:              
        lea esi, [str1]
        lea edi, [str3]
        mov ecx, str1len  ; selects the length of the first string as maximum for comparison
        rep cmpsb         ; comparison of ECX number of bytes
        mov eax, 4        ; does not modify flags 
        mov ebx, 1        ; does not modify flags 
        jne not_comb     ; checks ZERO flag
	jmp ifComb
not_comb:             
        lea esi, [str1]
        lea edi, [str4]
        mov ecx, str1len  ; selects the length of the first string as maximum for comparison
        rep cmpsb         ; comparison of ECX number of bytes
        mov eax, 4        ; does not modify flags 
        mov ebx, 1        ; does not modify flags 
        jne exit	  ; checks ZERO flag
	jmp ifPerm

ifComb:
	call getText_comb
        call print_rax_n

	call getText_comb_r
        call print_rax_r

        call print_rax_nsubr
	call fact_nsubr
	call fact_n
	call fact_r

	
	call mult_nsubr_r	
	call div_comb
	mov rax, 60
        mov rdi, 0
	syscall
getText_comb:
	prt_s "[value of n] Enter a number for the size of the set:"
	mov rax, 0
	mov rdi, 0
	mov rsi, ascii
	mov rdx, 16
	syscall
	mov byte [ascii-1+rax], 0
	jmp toInteger
getText_comb_r:
	prt_s "[value of r]Enter a number for the size of the sub-set:"
	mov rax, 0
	mov rdi, 0
	mov rsi, ascii
	mov rdx, 16
	syscall
	mov byte [ascii-1+rax], 0
	jmp toInteger

ifPerm:
	call getText_perm
        call print_rax_n

	call getText_perm_r
        call print_rax_r

        call print_rax_nsubr
	
	call fact_n
	call fact_nsubr
	
	call div_perm
	mov rax, 60
        mov rdi, 0
	syscall

getText_perm:
	prt_s "[value of n] Enter a number for the size of the set:"
	mov rax, 0
	mov rdi, 0
	mov rsi, ascii
	mov rdx, 16
	syscall
	mov byte [ascii-1+rax], 0
	jmp toInteger

getText_perm_r:
	prt_s "[value of r]Enter a number for the size of the sub-set:"
	mov rax, 0
	mov rdi, 0
	mov rsi, ascii
	mov rdx, 16
	syscall
	mov byte [ascii-1+rax], 0
	jmp toInteger

ifFact:
	call getText_fact
        call toInteger
        call print_rax_n
	call fact_n
	mov rax, 60
        mov rdi, 0

	jmp	continue_prog

getText_fact:
	prt_s "Enter a number for factorial:"
	mov rax, 0
	mov rdi, 0
	mov rsi, ascii
	mov rdx, 16
	syscall
	mov byte [ascii-1+rax], 0
	jmp toInteger

toInteger:
	mov rbx,10      ; for decimal scaling
	xor rax, rax    ; initializing result
	mov rcx, ascii  ; preparing for working with input

	.LL1:           ; loops the bytes
	movzx rdx, byte [rcx]   ; getting current byte (digit)

	test rdx, rdx   ; RDX == 0?
	jz .done        ; Yes: break

	inc rcx         ; for the next digit

	cmp rdx, '0'    ; if it's less than '0' is not a digit
	jb invalid

	cmp rdx, '9'    ; if it's greater than '9' is not a digit
	ja invalid

	sub rdx, '0'    ; getting decimal value

	add rax, rax
	lea rax, [rax + rax * 4]

	add rax, rdx    ; rax = rax + rdx
	jmp .LL1  ; repeat

	.done:

	ret

invalid:
        mov rax, 1
        mov rdi, 1
        mov rsi, text
        mov rdx, len
        syscall
        jmp main


print_rax_nsubr:
        mov     rax,[a]         
	sub	rax,[x]	
	mov	[o],rax
	mov	[i],rax
	mov	[j],rax
	prt_i	"Input value (n-r)"         ; invoke the print macro
	ret

print_rax_r:
        mov     [x],rax         
	mov	[y],rax
	mov	[n],rax
	prt_x	"Input value r"         ; invoke the print macro
	ret

print_rax_n:
        mov    	[a],rax         
	mov	[b],rax
	mov	[m],rax
	prt_a	"Input value n"         ; invoke the print macro
	ret



mult_nsubr_r:                           
        mov     rax,[i]         ; load a (must be rax for multiply)
        imul    qword [x]       ; signed integer multiply by b
        mov     [c],rax         ; store bottom half of product into c
        prt_c	"(n-r)!*r!"    ; invoke the print macro
	ret

fact_n:                           

	mov	rcx,[b]
        mov     rax,[a]         ; load a (must be rax for multiply)
	dec	rcx 
	mov	[b],rcx
        imul    qword [b]       ; signed integer multiply by b
        mov     [a],rax         ; load a (must be rax for multiply)
	push	rcx
        mov     [c],rax         ; store bottom half of product into c

	pop	rcx
	dec	rcx
	jnz	fact_n
	
	mac_a	"n!="    ; invoke the print mact
	ret
fact_r:                           ; c=a*b;

	mov	rcx,[y]
        mov     rax,[x]         ; load a (must be rax for multiply)
	dec	rcx 
	mov	[y],rcx
        imul    qword [y]       ; signed integer multiply by b
        mov     [x],rax         ; load a (must be rax for multiply)
	push	rcx
        mov     [c],rax         ; store bottom half of product into c

	pop	rcx
	dec	rcx
	jnz	fact_r
	
	mac_x	"r!="    ; invoke the print mact
	ret
fact_nsubr:                           ; c=a*b;

	mov	rcx,[j]
        mov     rax,[i]         ; load a (must be rax for multiply)
	dec	rcx 
	mov	[j],rcx
        imul    qword [j]       ; signed integer multiply by b
        mov     [i],rax         ; load a (must be rax for multiply)
	push	rcx
        mov     [c],rax         ; store bottom half of product into c

	pop	rcx
	dec	rcx
	jnz	fact_nsubr
	
	mac_i	"(n-r)!="    ; invoke the print mact
	ret
div_comb:                           
        mov     rax,[a]         ; load c
        mov     rdx,0           ; load upper half of dividend with zero
        idiv    qword [c]       ; divide double register edx rax by a
        mov     [c],rax         ; store quotient into c
        prt_c	"n!/(n-r)!*r!"         ; invoke the print macro

        pop     rbp             ; pop stack
        mov     rax,0           ; exit code, 0=normal
	jmp	continue_prog

div_perm:                           
        mov     rax,[a]         ; load c
        mov     rdx,0           ; load upper half of dividend with zero
        idiv    qword [c]       ; divide double register edx rax by a
        mov     [c],rax         ; store quotient into c
        prt_c	"n!/(n-r)!"         ; invoke the print macro

        pop     rbp             ; pop stack
        mov     rax,0           ; exit code, 0=normal
	jmp	continue_prog

continue_prog:
        prt_cont "null" 
	push rbp

	mov rax,0 
        mov rdi,0
        mov rsi,str1
        mov rdx,8
        syscall


        lea esi, [str1]
        lea edi, [str5]

        mov ecx, str5len  ; selects the length of the first string as maximum for comparison
        rep cmpsb         ; comparison of ECX number of bytes
        mov eax, 4        ; does not modify flags 
        mov ebx, 1        ; does not modify flags 
        jne exit       ; checks ZERO flag
	jmp main

exit:                 ; sane shutdown
        mov eax, 1
        mov ebx, 0
        int 80h
