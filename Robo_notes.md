## Notes & issues with Robofont

This is the first project for which I've used Robofont. I'm keeping a log of issues I run into, to be addressed (if possible) when I'm comfortable enough with the software to make the changes myself.

This is not intended to be passive-aggressive or otherwise directed at any of Robofont's contributors, just a record for my own purposes.

I'm planning to submit (some of) these to the Robofont forum, but I'd like to make sure beforehand that they are actual issues with the software, not just things I haven't yet figured out.

### Cosmetic
- Inspector and Output windows disappear when main application focus is lost.
- Space Center header and footer is blue-tinted.
- Inspector accordion menu sections use old OS X (10.9, 2013) gradient style.
- Glyph thumbnails in the Font Overview have an unnecessary gradient effect.
- Glyph Editor can only be scrolled one direction at a time.

### Functional
- Attempting to resize columns in the Font Overview (in Glyph List mode) causes a crash.
- There's no way to select on-curve and off-curve points in a single action.
- "Edit With Glyphs" toolbar button (in Font Overview) does nothing.
- Holding 'cmd' to drag one off-curve of a smooth point while constraining the opposite one does not fully constrain the opposite off-curve.
- Inputting non-ASCII characters into PostScript font name dialogue breaks test install but gives no indication beforehand.
- Many keyboard shortcuts cannot (as far as I can tell) be rebound, and many functions cannot have keyboard shortcuts assigned to them.
- Flip option in Copy/Swap To Layer dialog must be undone twice (once for each layer).
- Copying an image to the background doesn't work.
- Images sometimes act as if they're locked.
- When a UFO which contains an image is open, Robofont sometimes crashes without warning. Even if it's just idle in the background. Yes, I have checked the log file.
- Sometimes the ruler tool doesn't work.
- Sometimes UFO background data gets corrupted and I have to revert to an old version of a glyph.
- Sometimes selecting a glyph from the Font Overview causes a crash.