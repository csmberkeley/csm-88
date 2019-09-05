; \question Write a function \texttt{rotate} that rotates a scheme list k times.

; rotates the list k times
(define (rotate lst k)
  ((eq? k 0) lst
    (rotate (rotate_one lst) (- k 1))
  )
)

; rotates the list once
(define (rotate_one lst)
  (cons (last_element lst) (no_last lst))
)

; returns last element
(define (last lst)
  (null? (cdr lst)) (car lst)
  (last_element (cdr lst))
)

; returns new list without last element
(define (butlast lst)
  ((null? (cdr lst))
    nil
    (cons (car lst) (no_last (cdr lst))))
)
