resource "helm_release" "currency_converter" {
  name       = "currency-converter"
  repository = "file://../helm/currency-converter"
  chart      = "../helm/currency-converter"
  namespace  = "default"

  values = [
    file("../helm/currency-converter/values.yaml")
  ]
}
