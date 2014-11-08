	.file	"opt1.c"
	.section	.rodata
.LC0:
	.string	"elapsed = %d\n"
	.text
.globl main
	.type	main, @function
main:
	leal	4(%esp), %ecx
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%ecx
	subl	$36, %esp
	movl	$1258291200, (%esp)
	call	malloc
	movl	%eax, -12(%ebp)
	movl	$314572800, -8(%ebp)
	call	clock
	movl	%eax, -20(%ebp)
	jmp	.L2
.L3:
	movl	-8(%ebp), %eax
	sall	$2, %eax
	movl	%eax, %edx
	addl	-12(%ebp), %edx
	movl	-8(%ebp), %eax
	movl	%eax, (%edx)
	decl	-8(%ebp)
.L2:
	cmpl	$0, -8(%ebp)
	jg	.L3
	call	clock
	movl	%eax, -16(%ebp)
	movl	-20(%ebp), %edx
	movl	-16(%ebp), %eax
	subl	%edx, %eax
	movl	%eax, 4(%esp)
	movl	$.LC0, (%esp)
	call	printf
	addl	$36, %esp
	popl	%ecx
	popl	%ebp
	leal	-4(%ecx), %esp
	ret
	.size	main, .-main
	.ident	"GCC: (GNU) 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)"
	.section	.note.GNU-stack,"",@progbits
