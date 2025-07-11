{{- define "currency-converter.name" -}}
currency-converter
{{- end }}

{{- define "currency-converter.fullname" -}}
{{ include "currency-converter.name" . }}-{{ .Release.Name }}
{{- end }}
