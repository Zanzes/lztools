RC_SECTION_START_RIGHT = "START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
RC_SECTION_START_LEFT = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>"

RC_SECTION_END_RIGHT = "END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
RC_SECTION_END_LEFT = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===>"

SENTINEL_MARKER = "¤¤¤||||¤¤¤"

data_loader_bash_script = """#!/bin/bash

if [[ $(__lztools_resources has_output) == "True" ]]
then
    out_path="{}"
    source $out_path
    echo '' > $out_path
fi"""

Resources = r"git@bitbucket.org:zanzes/lzresources.git"