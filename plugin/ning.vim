
if !has('python')
    echo "Error: Required vim 73 compiled with +python"
    finish
endif

if !exists('s:vimrst_did_init')
    let s:script_path = substitute(expand("<sfile>:p"),'\','/','g')
    let s:script_dir = substitute(expand("<sfile>:p:h"),'\','/','g')
    let s:vimrst_dir = s:script_dir.'/../py'

python << EOF
import sys, vim
#print vim.eval("s:vimrst_dir")

if not vim.eval("s:vimrst_dir") in sys.path:
    sys.path.append(vim.eval("s:vimrst_dir"))
import vimrst
import rst_imglink

EOF


    let s:vimrst_did_init = 1
endif


autocmd BufWritePre *.rst call FormatSectionTitle()
"noremap <silent>  <C-S-c> :call format_section_title()<CR>
" auto ChangeToThis
noremap <C-S-c> :call FormatSectionTitle()<CR>


command! -nargs=* RstInsertImgLink call RstInsertImgLink( '<args>' )
