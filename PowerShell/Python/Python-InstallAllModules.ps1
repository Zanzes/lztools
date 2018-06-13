function Python-InstallAllModules
{
    [CmdletBinding(DefaultParameterSetName='Parameter Set 1')]
    [OutputType([String])]
    Param
    (
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=0, ParameterSetName='Parameter Set 1')]
        [Alias("Dev")]
        [switch]
        $Develop = $false,
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=0, ParameterSetName='Parameter Set 2')]
        [Alias("Remove")]
        [switch]
        $Uninstall = $false
    )

    $pkg_dir = "C:\Python27\Lib\site-packages`\";
    if (-not [System.IO.Directory]::Exists($pkg_dir)) {
        $pkg_dir = "C:\Python27amd64\Lib\site-packages`\";
    }

    $pkgs = New-Object System.Collections.ArrayList;
    

    Get-ChildItem | % `
    {
        if ([System.IO.File]::Exists($_.FullName + "`\setup.py")) {
            $null = $pkgs.Add($_.Name);
        }
    }

    if ($Uninstall)
    {
        foreach ($pkg in $pkgs)
        {
            try
            {
                Python-InstallModule -Name $pkg -Uninstall;
            }
            catch { }
        }
        return;
    }

    (Get-ChildItem -Path $pkg_dir) | % `
    {
        $n = $_.Name;
        $f = $_.FullName;
        ($pkgs) | % `
        {
            if ($n -like "$_*") {
                Remove-Item -Path $f -Force -Recurse; 
            }
        }
    }

    $pkgs | % `
    {
    
        if ($Develop)
        {
            Python-InstallModule $_ -Develop;
        }
        else
        {
            Python-InstallModule $_;
        }
    }

}