local t = {}
local file = "../Input/day2.in"
for s in io.lines(file) do
    local x = {}
    s:gsub(".", function(c) table.insert(x, c) end)
    table.insert(t, x)
end
local twos = 0
local trees = 0

for i,j in pairs(t) do
    local o = {}
    for x, y in pairs(j) do
        if o[y] == nil then
            o[y] = 1
        else
            o[y] = o[y] + 1
        end
    end
    local tree = true
    local two = true
    for x,y in pairs(o) do
        if y == 3 and tree then
            tree = false
            trees = trees + 1
        end
        if y == 2 and two then
            two = false
            twos = twos + 1
        end
    end
end

io.write(twos * trees, "\n")

table.sort(t, function(a, b)  return table.concat(a) < table.concat(b) end)

for i = 1, #t -1 do
    local diff = true
    local out = ""
    for j=1, #t[i] do
        if t[i][j] ~= t[i+1][j] and diff then
            diff = false
        elseif t[i][j] ~= t[i+1][j] and not diff then
            out = ""
            break
        else
            out = out .. t[i][j]
        end
    end
    if out ~= "" then
        io.write(out, "\n")
        break
    end
end
