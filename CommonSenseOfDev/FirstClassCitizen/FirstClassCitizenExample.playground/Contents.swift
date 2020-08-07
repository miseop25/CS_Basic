import UIKit

func firstClassCitizen(test: String) -> String {
    print("1")
    return test
}


func fccTest(test: String) {
    print("2")
}
let fcc = firstClassCitizen
fccTest(test: fcc("Hello"))

func returnFunc() -> String {
    return firstClassCitizen(test: "3")
}

let f:(Data) -> Void = { data in
    // ...
}
f
fcc("hello")


returnFunc()
