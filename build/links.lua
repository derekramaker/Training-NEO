-- Repo-relative links (e.g. docs/templates/bsa/02-requirements.md) do not resolve once a page
-- is pasted into OneNote, so render them as inline code showing the path instead.
function Link(el)
  local t = el.target
  if t:match("^https?://") or t:match("^mailto:") or t:match("^#") then
    return el
  end
  local text = pandoc.utils.stringify(el.content)
  if text == t then
    return pandoc.Code(t)
  end
  local out = el.content
  table.insert(out, pandoc.Str(" ("))
  table.insert(out, pandoc.Code(t))
  table.insert(out, pandoc.Str(")"))
  return out
end
