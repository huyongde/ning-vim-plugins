

func PreviewWord()
  if &previewwindow          " don't do this in the preview window
    return
  endif
  let w = expand("<cword>")      " get the word under cursor
  if w =~ '\a'           " if the word contains a letter

    let currentWindow = winnr()
    echom currentWindow
    " Delete any existing highlight before showing another tag
    silent! wincmd P         " jump to preview window
    if &previewwindow            " if we really get there...
      match none         " delete existing highlight
      wincmd p           " back to old window
    endif

    " Try displaying a matching tag for the word under the cursor
    try
       exe "ptag " . w
    catch
      silent! exe currentWindow . "wincmd w"
      return
    endtry

    silent! wincmd P         " jump to preview window
    if &previewwindow        " if we really get there...
      if has("folding")
        "echom 'foldopen'
        silent! .foldopen!           " don't want a closed fold
      endif

      call search("$", "b")      " to end of previous line
      let w = substitute(w, '\\', '\\\\', "")
      call search('\<\V' . w . '\>') " position cursor on match

      " Add a match highlight to the word at this position
      hi previewWord term=bold ctermbg=green guibg=green
      exe 'match previewWord "\%' . line(".") . 'l\%' . col(".") . 'c\k*"'
      "wincmd p           " back to old window(not always)
      silent! exe currentWindow . "wincmd w"
    endif

  endif
endfun

func SetupSI()
    set updatetime=500
    set previewheight=10
    au! CursorHold *.cpp nested call PreviewWord()
    au! CursorHold *.hpp nested call PreviewWord()
    au! CursorHold *.[ch] nested call PreviewWord()
endfun

command! SI call SetupSI()

