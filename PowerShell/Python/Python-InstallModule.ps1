function Python-InstallModule()
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
        $Develop = $false,
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=0, ParameterSetName='Parameter Set 2')]
        [string]
        $Name = $null,
        [Parameter(Mandatory=$false, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, ValueFromRemainingArguments=$false, Position=1, ParameterSetName='Parameter Set 2')]
        [Alias("Remove")]
        [switch]
        $Uninstall = $false
    )

    if($Uninstall)
    {
        Invoke-Command -ErrorAction SilentlyContinue { cmd /c "python -m pip uninstall $Name -y" };
        return;   
    }

    if ($Path -eq $null) {
        $Path = (Resolve-Path .).Path
    }
    $mname = [System.IO.DirectoryInfo]::new($Path).Name;
    
    $orig_p = (Resolve-Path .).Path;
    cd $Path;
    
    $ccmd = "install";
    if ($Develop -ne $null)
    {
        if ($Develop)
        {
            $ccmd="develop";
        }
    }
    Invoke-Command -ErrorAction SilentlyContinue { cmd /c "python setup.py $ccmd" };
    try
    {
        Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "build" -ErrorAction SilentlyContinue) -ErrorAction SilentlyContinue
    } catch { }
    try
    {
        Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "dist" -ErrorAction SilentlyContinue) -ErrorAction SilentlyContinue
    } catch { }
    try
    {
        $n = [System.IO.DirectoryInfo]::new((Resolve-Path . -ErrorAction SilentlyContinue)).Name
        Remove-Item -Recurse -Force -Path (Resolve-Path -Relative -Path "$n.egg-info" -ErrorAction SilentlyContinue)
    } catch {  }
    
    cd $orig_p

}