singleExpression
 | singleExpression '+' singleExpression                                                   /// UnaryPlusExpression
 | singleExpression '-' singleExpression                                                   /// UnaryMinusExpression
 | '(' '~' singleExpression ')'                                               /// BitNotExpression
 | '(' '!' singleExpression ')'                                               /// NotExpression
 | singleExpression '*' singleExpression
 | singleExpression '/' singleExpression
 | singleExpression '%' singleExpression                                      /// MultiplicativeExpression
 | singleExpression '+' singleExpression
 | singleExpression '-' singleExpression                                      /// AdditiveExpression
 | singleExpression '<<' singleExpression
 | singleExpression '>>' singleExpression
 | singleExpression '>>>' singleExpression              /// BitShiftExpression
 | singleExpression '<'  singleExpression          /// RelationalExpression
 | singleExpression '>'  singleExpression          /// RelationalExpression
 | singleExpression '<=' singleExpression          /// RelationalExpression
 | singleExpression '>=' singleExpression          /// RelationalExpression
 | singleExpression '==' singleExpression
 | singleExpression '!=' singleExpression
 | singleExpression '===' singleExpression
 | singleExpression '!==' singleExpression      /// EqualityExpression
 | singleExpression '&' singleExpression                                      /// BitAndExpression
 | singleExpression '^' singleExpression                                      /// BitXOrExpression
 | singleExpression '|' singleExpression                                      /// BitOrExpression
 | singleExpression '&&' singleExpression                                     /// LogicalAndExpression
 | singleExpression '||' singleExpression                                     /// LogicalOrExpression
 | '(' singleExpression ')'                                                   /// ParenthesizedExpression
 | number
 | 'null'
 | 'true'
 | 'false'
 | 'undefined'
 ;
