# Light control

## Examples

turn on the light just in 'corridor1' room
```
curl 'http://10.52.100.104:5002/?state=all~off,corridor1~on'
```

turn off all the light
```
curl 'http://10.52.100.104:5002/?state=all~off'
```
