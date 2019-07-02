; File name: fibinachi_nasm64bit.asm
; Compile with command and run: nasm -felf64 fibinachi_nasm64bit.asm && gcc -no-pie fibinachi_nasm64bit.o && ./a.out

; fibinachi numbers NASM
; Anton Rakos, R11464913
        
        global main
        extern printf

        section .data
state:  db '    Fibinachi number ', '%ld', 0  ; The State of the printed Fibinachi number, starting at 1. 
format: db 58, '%1ld', 46,10, 0  
title:  db 'Fibinachi Numbers, hard coded to the 10th number', 10, 0 ; The title of the program, printed at the start of the program.
        
        section .text
main:
        push rbp                ; rbp is a NASM 64 bit Preserved register, this serves as the stack pointer
        mov rdi, title          ; In Linux rdi is a Scratch register and the first function aregument.  The first argument is a pointer to title
        mov rax, 0              ; Values are returned from functions in rax. No vector registers in use.
        call printf             ; Calling printf here will print the title.

        mov rcx, 10             ; rcx is a scratch register and used in this case to countdown from N to 0.  In this program N is hard coded to 10.
        mov rax, 0              ; rax will hold the current number in the count down.
        mov rbx, 1              ; rbx will hold the next number
        mov r13, 0              ; r13 is a preserved register in 64-bit NASM
print:
        
        inc r13
        push rax
        push rcx
        mov rdi, state          ; This indents the output of printf by 10 spaces. 
        mov rsi, r13            ; In Linux rsi is a scratch register used to pass the second function argument.
        mov eax, 0              ; no vector registers in use

        call printf
        pop rcx
        pop rax

        push rax
        push rcx
        mov rdi, format         ; This indents the output of printf by 10 spaces. 
        mov rsi, rax            ; In Linux rsi is a scratch register used to pass the second function argument.
        mov eax, 0              ; no vector registers in use
        call printf
        pop rcx
        pop rax
        
        mov rdx, rax            ; save the current number of rax to the rdx register
        mov rax, rbx            ; rax is now updated with the contents of rbx
        add rbx, rdx            ; adds the saved rdx to rbx the new next number
        dec rcx                 ; count down
        jnz print               ; if not done counting, do some more

        pop rbp                 ; restore stack
        mov rax, 0              ; normal exit
        ret

