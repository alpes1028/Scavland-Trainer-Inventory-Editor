-- Build: 922293ee0a081bfd90d6d75d9c99f4f1
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
