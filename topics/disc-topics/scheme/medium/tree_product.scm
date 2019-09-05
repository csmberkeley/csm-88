; Returns new tree where each entry is the product of itself and its parents value. The value of the tree root remains unchanged.
(define (product-tree tree)

  ; does the hard work
  (define (helper tree k)
    ((is_leaf tree)
      (tree (* (root tree) k) ())
      (tree (* (root tree) k) (map (branches t) (root tree)))
    )

  ; returns a list of trees, which is built by calling product-tree on all children
  (def (map fn branches k)
    ((null? branches)
      nil
      (cons (fn (car branches) k) (map fn (cdr branches) k))
    )
  )

  (helper tree 1)
)
