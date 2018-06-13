function Python-CreateInstaller()
{
    [CmdletBinding(DefaultParameterSetName='Parameter Set 1')]
    [OutputType([String])]
    Param
    (
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=0, ParameterSetName='Parameter Set 1')]
        [string]
        $Path = $null,
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=1, ParameterSetName='Parameter Set 1')]
        [Alias("Dev")]
        [switch]
        $Develop = $null
    )
    if ($Path -eq $null) {
        $Path = $PSScriptRoot
    }

    $mname = [System.IO.DirectoryInfo]::new($Path).Name;
    
    $orig_p = (Resolve-Path .).Path;
    cd $Path;

    Invoke-Command -ErrorAction SilentlyContinue `
    {
        cmd /c "python setup.py bdist_msi";
    }

    $col = [System.IO.Directory]::EnumerateFiles((Resolve-Path "dist").Path, "*.msi", [System.IO.SearchOption]::AllDirectories)
    foreach ($item in $col)
    {
        $target = $(Resolve-Path "..\..\Installers").Path+"\$mname.msi";
        if ([System.IO.File]::Exists($target))
        {
            Remove-Item -Path $target;
        }
        [System.IO.Directory]::Move($item, $target);
    }

    try { Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "build" -ErrorAction SilentlyContinue) -ErrorAction SilentlyContinue } catch { }
    try { Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "dist" -ErrorAction SilentlyContinue) -ErrorAction SilentlyContinue } catch { }
    try {
        $n = [System.IO.DirectoryInfo]::new((Resolve-Path . -ErrorAction SilentlyContinue)).Name;
        Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "$n.egg-info" -ErrorAction SilentlyContinue);
    } catch {  }
    
    cd $orig_p;

}
