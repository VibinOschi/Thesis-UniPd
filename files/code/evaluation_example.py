def generate_binary_histogram(model_id, acc_prevision, loss_prevision):
    fig2, histogram = plt.subplots()
    histogram.set_ylabel('Number of predictions')
    histogram.set_xlabel('prediction')
    histogram.hist([[x1[0] for x1 in acc_prevision.tolist()], [x2[0] for x2 in loss_prevision.tolist()]], edgecolor='#111', linewidth=0.5, label=['Accuracy_Model', 'Loss_Model'])
    histogram.legend()
    plt.savefig(ConfigGetter().get_models_path() + 'model_' + model_id + '/histogram_model_' + model_id + '.png')