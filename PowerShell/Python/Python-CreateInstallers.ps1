function Python-CreateAllInstallers
{
    [CmdletBinding(DefaultParameterSetName='Parameter Set 1')]
    [OutputType([String])]

    $pkgs = New-Object System.Collections.ArrayList;
    
    Get-ChildItem | % `
    {
        if ([System.IO.File]::Exists($_.FullName + "`\setup.py")) {
            $null = $pkgs.Add($_.Name);
        }
    }

    $pkgs | % `
    {
        Python-CreateInstaller $_
    }

}
