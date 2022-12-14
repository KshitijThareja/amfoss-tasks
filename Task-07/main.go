package main
import "fmt" 

func increment(num1 int) {
	fmt.Printf("increment called")
	inc_total := num1 + 1
	return inc_total
	
}
func decrement(num2 int) {
	dec_total := num2 - 1
	return dec_total
}  
func reset(num3 int) {
	res_total := 0
	return res_total

}

func main() {        
	data := 0
	f := js.Global.Get("document").Call("getElementById", "int").SetInnerHTML(data)

	a:= increment(data)
	f := js.Global.Get("document").Call("getElementById", "int").SetInnerHTML(a)

	data:=a

	b:= decrement(data)
	f := js.Global.Get("document").Call("getElementById", "int").SetInnerHTML(b)
	data:=b

	c:= reset(data)
	f := js.Global.Get("document").Call("getElementById", "int").SetInnerHTML(c)

	}


	



