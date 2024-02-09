using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class LoseMenuScript : MonoBehaviour
{

    [SerializeField] private BattleManager battleManager;
    [SerializeField] private GameObject loseScreen;
    [SerializeField] private GameObject winPopUp;
    [SerializeField] private GameObject battleHUD;
    // Start is called before the first frame update
    void Start()
    {
        battleManager.OnLose.AddListener(LoseScreen);
        battleManager.OnWin.AddListener(WinPopUp);
    }

    private void LoseScreen()
    {
        battleHUD.SetActive(false);
        loseScreen.SetActive(true);
    }

    private void WinPopUp()
    {
        battleHUD.SetActive(false);
        winPopUp.SetActive(true);
    }

    public void MainMenu()
    {
        SceneLoader.Load(SceneLoader.Scene.MainMenu);
        Time.timeScale = 1;

    }

    public void Retry()
    {
        GameManager.Instance.ResetCharacterPos();
        SceneLoader.Load(SceneLoader.Scene.StartMap);
        Time.timeScale = 1;
    }

    public void Continue()
    {
        SceneLoader.Load(SceneLoader.Scene.StartMap);
        Time.timeScale = 1;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
